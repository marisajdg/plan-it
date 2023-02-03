# -------------------------------------
# Plan It
# Web Service
# 'database.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from . import database_connection
import pymongo
import models
import constants

class Database:

    def __init__(self, database_client: pymongo.MongoClient):

        database_handle = database_client[constants.DB_NAME]

        self.database_sessions_collection = database_handle[constants.DB_SESSIONS_COLLECTION]
        self.database_users_collection = database_handle[constants.DB_USERS_COLLECTION]
        self.database_lists_collection = database_handle[constants.DB_LISTS_COLLECTION]
        self.database_places_collection = database_handle[constants.DB_PLACES_COLLECTION]

    def insert_user(self, user: models.User):

        user_schema = models.UserSchema()
        result = user_schema.dump(user)

        self.database_users_collection.insert_one(result)
    
    def username_exists(self, username: str) -> bool:

        return self.database_users_collection.find_one( { constants.USERNAME: username } ) != None

    def email_exists(self, email: str) -> bool:

        return self.database_users_collection.find_one( { constants.EMAIL: email } ) != None

    def get_user_by_email(self, email: str):

        return self.database_users_collection.find_one( { constants.EMAIL: email } )

    def get_user_by_user_id(self, user_id: str):

        return self.database_users_collection.find_one( { constants.USER_ID: user_id } )

database = Database(database_client=database_connection.database_client)
