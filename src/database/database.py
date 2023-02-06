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

    @classmethod
    def insert_user(cls, user: models.User):

        user_schema = models.UserSchema()
        result = user_schema.dump(user)

        cls.database_users_collection.insert_one(result)
    
    @classmethod
    def username_exists(cls, username: str) -> bool:

        return cls.database_users_collection.find_one( { constants.Text.USERNAME: username } ) != None

    @classmethod
    def email_exists(cls, email: str) -> bool:

        return cls.database_users_collection.find_one( { constants.Text.EMAIL: email } ) != None

    @classmethod
    def get_user_by_email(cls, email: str):

        return cls.database_users_collection.find_one( { constants.Text.EMAIL: email } )

    @classmethod
    def get_user_by_user_id(cls, user_id: str):

        return cls.database_users_collection.find_one( { constants.Text.USER_ID: user_id } )
