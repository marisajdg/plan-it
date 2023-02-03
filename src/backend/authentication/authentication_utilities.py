# -------------------------------------
# Plan It
# Web Service
# 'authentication_utilities.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from flask import session
from database.database_connection import database
from functools import wraps
import constants

def username_exists(username: str) -> bool:

    users_collection = database[constants.DB_USERS_COLLECTION]

    return users_collection.find_one( { constants.USERNAME: username } ) != None

def email_exists(email: str) -> bool:

    users_collection = database[constants.DB_USERS_COLLECTION]

    return users_collection.find_one( { constants.EMAIL: email } ) != None

def get_user_by_email(email: str):

    users_collection = database[constants.DB_USERS_COLLECTION]

    return users_collection.find_one( { constants.EMAIL: email } )

def get_user_by_user_id(user_id: str):

    users_collection = database[constants.DB_USERS_COLLECTION]

    return users_collection.find_one( { constants.USER_ID: user_id } )

# Authentication Decorator
def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        try:
           
            user_id = session.get(constants.USER_ID)

            if(not user_id):
                return {
                    constants.ERROR_MESSAGE: constants.ERROR_USER_NOT_AUTHENTICATED
                }, constants.HTTP_UNAUTHORIZED_CODE

        except:
            
            return {
                constants.ERROR_MESSAGE: constants.ERROR_USER_NOT_AUTHENTICATED
            }, constants.HTTP_UNAUTHORIZED_CODE

        return f(*args, **kwargs)

    return decorator
    