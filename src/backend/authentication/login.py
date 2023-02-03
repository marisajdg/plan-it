# -------------------------------------
# Plan It
# Web Service
# 'login.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from werkzeug.security import check_password_hash
from . import authentication_utilities as auth
import constants

def password_matches(email: str, password: str) -> bool:

    user = auth.get_user_by_email(email) 

    hashed_password = user[constants.PASSWORD]

    return check_password_hash(pwhash=hashed_password, password=password)