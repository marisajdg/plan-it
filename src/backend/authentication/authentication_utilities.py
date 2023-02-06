# -------------------------------------
# Plan It
# Web Service
# 'authentication_utilities.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from flask import session
from database.database import Database
from functools import wraps
import constants

# Authentication Decorator
def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        try:
           
            user_id = session.get(constants.USER_ID)

            if(not user_id):
                return {
                    constants.ERROR_MESSAGE: constants.ERROR_USER_NOT_AUTHENTICATED
                }, constants.HTTP_UNAUTHORIZED_CODE

        except:
            
            return {
                constants.ERROR_MESSAGE: constants.ERROR_USER_NOT_AUTHENTICATED
            }, constants.HTTP_UNAUTHORIZED_CODE

        return f(*args, **kwargs)

    return decorator
    