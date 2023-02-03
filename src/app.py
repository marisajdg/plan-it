# -------------------------------------
# Plan It
# Web Service
# 'app.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from flask import Flask
import constants

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host=constants.SERVER_IP, port=constants.SERVER_PORT, debug=True)