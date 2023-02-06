# -------------------------------------
# Plan It
# Web Service
# 'app.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from flask import Flask
from flask_sessionstore import Session
from server_configuration import ServerConfiguration
import constants

app = Flask(__name__)

app.config.from_object(ServerConfiguration)
server_session = Session(app)

import backend.authentication.authentication_endpoints

if __name__ == '__main__':
    app.run(host=constants.Configuration.SERVER_IP, port=constants.Configuration.SERVER_PORT, debug=constants.Configuration.SERVER_DEBUG_ENABLED)