#!/usr/bin/env python

import unittest
from src import create_app, get_mdb, get_mdb_client
from config import Config
from passlib.hash import pbkdf2_sha256
import uuid

class TestConfig(Config):
    TESTING = True
    DB_NAME = 'test_login'


class TestUserLogin(unittest.TestCase):
    def setUp(self):
        self._app = create_app(TestConfig)
        self._app_context = self._app.app_context()
        self._app_context.push()
        self._testmdb = get_mdb()


    def tearDown(self):
        get_mdb_client().drop_database(self._testmdb)
        self._app_context.pop()


    def test_login(self):
        # Add a test user in database
        user_id = uuid.uuid4().hex
        user_name = 'Aniket Meshram'
        user_email = 'aniket@test.com'
        user_passwd = 'some-password'
        test_user = {
            "_id": user_id,
            "name": user_name,
            "email": user_email,
            "password": pbkdf2_sha256.hash(user_passwd)
        }
        self._testmdb.lusers.insert_one(test_user)

        with self._app.test_client() as tc:
            # import pudb; pu.db
            # Test client call for login
            resp = tc.post('/user/login', data=dict(
                email = user_email,
                password = user_passwd
            ))

            # Check if session contains logged_in and user attributes
            del test_user['password']
            with tc.session_transaction() as ssn:
                self.assertEqual(ssn['logged_in'], True, "Session's logged_in attribute should be True")
                self.assertEqual(ssn['user'], test_user, "Session's user attribute should contain test_user")

            # Signout and delete the document from collection
            resp = tc.get('/user/signout')
            res = self._testmdb.lusers.delete_one({ "name": user_name })

            # Check if the entry is deleted
            self.assertEqual(res.deleted_count, 1, "Only 1 document should be deleted")
