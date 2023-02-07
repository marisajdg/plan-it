# -------------------------------------
# Plan It
# Web Service
# 'database.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from .database_connection import database_client
import pymongo
import models
import constants

class Database:

    # Class Variables
    database_sessions_collection = database_client[constants.Configuration.DB_NAME][constants.Configuration.DB_SESSIONS_COLLECTION]
    database_users_collection = database_client[constants.Configuration.DB_NAME][constants.Configuration.DB_USERS_COLLECTION]
    database_lists_collection = database_client[constants.Configuration.DB_NAME][constants.Configuration.DB_LISTS_COLLECTION]
    database_places_collection = database_client[constants.Configuration.DB_NAME][constants.Configuration.DB_PLACES_COLLECTION]        


    '''
    p1: user: User object to add to the Database
    return: Boolean indicating the status of the operation; True if the operation was succesful, False otherwise
    '''
    @classmethod
    def insert_user(cls, user: models.User) -> bool:

        try:

            user_schema = models.UserSchema()
            user_json = user_schema.dump(user)
            
            return cls.database_users_collection.insert_one(user_json).acknowledged

        except:

            return False


    '''
    p1: email: Email to look for in the Database
    return: User object if found, None otherwise
    '''
    @classmethod
    def get_user_by_email(cls, email: str) -> models.User:

        try:

            user_json = cls.database_users_collection.find_one( { constants.Text.EMAIL: email } )
            if(user_json == None): return None

            user_json.pop(constants.Text.OBJECT_ID)

            user_schema = models.UserSchema()
            return user_schema.load(user_json)

        except:

            return None


    '''
    p1: user_id: User ID to look for in the Database
    return: User object if found, None otherwise
    '''
    @classmethod
    def get_user_by_user_id(cls, user_id: str) -> models.User:

        try:

            user_json = cls.database_users_collection.find_one( { constants.Text.USER_ID: user_id } )
            if(user_json == None): return None

            user_json.pop(constants.Text.OBJECT_ID)

            user_schema = models.UserSchema()
            return user_schema.load(user_json)

        except:

            return None
    

    '''
    p1: username: Username to look for in the Database
    return: Boolean indicating the status of the operation; True if exists, False otherwise
    '''
    @classmethod
    def username_exists(cls, username: str) -> bool:

        return cls.database_users_collection.find_one( { constants.Text.USERNAME: username } ) != None


    '''
    p1: email: Email to look for in the Database
    return: Boolean indicating the status of the operation; True if exists, False otherwise
    '''
    @classmethod
    def email_exists(cls, email: str) -> bool:

        return cls.database_users_collection.find_one( { constants.Text.EMAIL: email } ) != None
