# -------------------------------------
# Plan It
# Web Service
# 'server_configuration.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from database.database_connection import database_client
from datetime import timedelta
import constants
import os

class ServerConfiguration:

    SECRET_KEY = str(os.getenv(constants.Configuration.SECRET_KEY))
    SESSION_TYPE = constants.Configuration.MONGO_DB
    SESSION_MONGODB = database_client
    SESSION_MONGODB_DB = str(os.getenv(constants.Configuration.DB_NAME))
    SESSION_MONGODB_COLLECT = constants.Configuration.DB_SESSIONS_COLLECTION
    PERMANENT_SESSION_LIFETIME = timedelta(days=constants.Numerics.SESSION_LIFETIME_DAYS)
    SESSION_USE_SIGNER = constants.Configuration.SESSION_USE_SIGNER
