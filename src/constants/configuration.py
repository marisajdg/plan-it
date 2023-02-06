# -------------------------------------
# Plan It
# Web Service
# 'configuration.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

# Configuration Constants
class Configuration:

    SERVER_IP = '0.0.0.0'
    SERVER_PORT = 5000
    SECRET_KEY = 'SECRET_KEY'
    MONGO_DB = 'mongodb'
    SESSION_USE_SIGNER = True
    SERVER_DEBUG_ENABLED = True
    DB_CONNECTION_URI = 'DB_CONNECTION_URI'
    DB_NAME = 'DB_NAME'
    DB_SESSIONS_COLLECTION = 'sessions'
    DB_USERS_COLLECTION = 'users'
    DB_LISTS_COLLECTION = 'lists'
    DB_PLACES_COLLECTION = 'places'