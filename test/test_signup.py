#!/usr/bin/env python

import unittest
from src import create_app, get_mdb, get_mdb_client
from config import Config
from passlib.hash import pbkdf2_sha256
import uuid

class TestConfig(Config):
    TESTING = True
    DB_NAME = 'test_signup'


class TestUserSignup(unittest.TestCase):
    def setUp(self):
        self._app = create_app(TestConfig)
        self._app_context = self._app.app_context()
        self._app_context.push()
        self._testmdb = get_mdb()
        

    def tearDown(self):
        get_mdb_client().drop_database(self._testmdb)
        self._app_context.pop()


    def test_signup(self):
        user_name = 'Aniket Meshram'
        user_email = 'aniket@test.com'
        user_passwd = 'some-passwd'
            
        with self._app.test_client() as tc:
            # import pudb; pu.db
            # Test client call to signup
            resp = tc.post('/user/signup', data=dict(
                name = user_name,
                email = user_email,
                password = user_passwd
            ))
            
            # Check user data in the database
            self.assertEqual(self._testmdb.lusers.count_documents({ "name": user_name }), 1, "Should be only 1 document")
            user_doc = self._testmdb.lusers.find_one({ "email": user_email })
            if user_doc:
                self.assertEqual(user_doc['name'], user_name, "Names mismatch!")
                self.assertEqual(user_doc['email'], user_email, "Email mismatch!")
                self.assertTrue(pbkdf2_sha256.verify(user_passwd, user_doc['password']), "Password mismatch!")
                with tc.session_transaction() as ssn:
                    self.assertEqual(ssn['logged_in'], True, "Session's logged_in attribute should be True")
            else:
                self.assertTrue(False, "No user document found in DB!")

            # Signout and delete the document from collection
            resp = tc.get('/user/signout')
            res = self._testmdb.lusers.delete_one({ "name": user_name })

            # Check if the entry is deleted
            self.assertEqual(res.deleted_count, 1, "Only 1 document should be deleted")
