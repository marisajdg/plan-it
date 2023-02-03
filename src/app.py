# -------------------------------------
# Plan It
# Web Service
# 'app.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)