# -------------------------------------
# Plan It
# Web Service
# 'app.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from flask import Flask
from flask_sessionstore import Session
from datetime import timedelta
from database.database_connection import database_client
import constants
import os

app = Flask(__name__)

app.config[constants.SECRET_KEY] = str(os.getenv(constants.SECRET_KEY))
app.config[constants.SESSION_TYPE] = 'mongodb'
app.config[constants.SESSION_MONGODB] = database_client
app.config[constants.SESSION_MONGODB_DB] = str(os.getenv(constants.DB_NAME))
app.config[constants.SESSION_MONGODB_COLLECT] = constants.DB_SESSIONS_COLLECTION
app.config[constants.PERMANENT_SESSION_LIFETIME] = timedelta(days=constants.SESSION_LIFETIME_DAYS)
app.config[constants.SESSION_USE_SIGNER] = True

server_session = Session(app)

import backend.authentication.authentication_endpoints

if __name__ == '__main__':
    app.run(host=constants.SERVER_IP, port=constants.SERVER_PORT, debug=True)