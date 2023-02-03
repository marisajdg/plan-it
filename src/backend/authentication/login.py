# -------------------------------------
# Plan It
# Web Service
# 'login.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from werkzeug.security import check_password_hash
from database.database import database
import constants

def password_matches(email: str, password: str) -> bool:

    user = database.get_user_by_email(email) 

    hashed_password = user[constants.PASSWORD]

    return check_password_hash(pwhash=hashed_password, password=password)