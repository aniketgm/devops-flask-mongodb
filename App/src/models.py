from flask import jsonify, request, session, redirect
from flask import current_app as capp
from passlib.hash import pbkdf2_sha256
from src import get_mdb
import uuid

class User:

    # Initialize db instance for the class
    def __init__(self):
        self._mdb = get_mdb()


    # Start session for a successful login
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200


    # Sign up into session and add new user details in database
    def signup(self, luser): 
        if luser:
            # Check if user already exist
            if self._mdb.lusers.find_one({ "email": luser['email'] }):
                return jsonify({ "error": "Email already in use" }), 400

            # Encrypt password
            luser['password'] = pbkdf2_sha256.hash(luser['password'])

            # Add/Update and entry into the database
            if self._mdb.lusers.insert_one(luser):
                return self.start_session(luser)
            
        return jsonify({ "error": "Signup failed!" }), 400


    # Sign out from session
    def signout(self):
        session.clear()
        return redirect('/')


    # Log into session
    def login(self, luser):
        if luser:
            # Get user details from database
            user = self._mdb.lusers.find_one({ "email": luser['email'] })

            # Start session if passwords match
            if user and pbkdf2_sha256.verify(luser['password'], user['password']):
                return self.start_session(user)

        return jsonify({ "error": "Login failed!"}), 401
