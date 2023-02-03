# -------------------------------------
# Plan It
# Web Service
# 'authentication_endpoints.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from __main__ import app
from bson.json_util import dumps
from flask import request, session
from database.database import database
from . import register
from . import login
import constants

# Register User Endpoint
@app.put(constants.REGISTER_ENDPOINT)
def register_user():

#try:
    
    # Verify JSON Content Type
    if(not request.is_json):
        return {
            constants.ERROR_MESSAGE: constants.ERROR_CONTENT_NOT_JSON
        }, constants.HTTP_BAD_REQUEST_CODE

    user_data = request.get_json()

    if(not((constants.USERNAME in user_data) and (constants.EMAIL in user_data) and (constants.PASSWORD in user_data))):
        return {
            constants.ERROR_MESSAGE: constants.ERROR_MISSING_FIELDS
        }, constants.HTTP_BAD_REQUEST_CODE

    username = user_data[constants.USERNAME]
    email = user_data[constants.EMAIL]
    password = user_data[constants.PASSWORD]
    
    if(not register.valid_username(username)):
        return {
            constants.ERROR_MESSAGE: constants.ERROR_INVALID_USERNAME
        }, constants.HTTP_BAD_REQUEST_CODE

    if(not register.valid_email(email)):
        return {
            constants.ERROR_MESSAGE: constants.ERROR_INVALID_EMAIL
        }, constants.HTTP_BAD_REQUEST_CODE

    if(not register.valid_password(password)):
        return {
            constants.ERROR_MESSAGE: constants.ERROR_INVALID_PASSWORD
        }, constants.HTTP_BAD_REQUEST_CODE

    if(database.username_exists(username)):
        return {
            constants.ERROR_MESSAGE: constants.ERROR_USERNAME_EXISTS
        }, constants.HTTP_CONFLICT_CODE

    if(database.email_exists(email)):
        return {
            constants.ERROR_MESSAGE: constants.ERROR_EMAIL_EXISTS
        }, constants.HTTP_CONFLICT_CODE

    register.register_user(username, email, password)

    user = database.get_user_by_email(email)

    session[constants.USER_ID] = user[constants.USER_ID]

    user.pop(constants.OBJECT_ID)
    user.pop(constants.USER_ID)
    user.pop(constants.PASSWORD)

    return dumps(user), constants.HTTP_OK_CODE

#except:

    return {
        constants.ERROR_MESSAGE: constants.ERROR_REGISTER
    }, constants.HTTP_INTERNAL_ERROR_CODE

# Login User Endpoint
@app.post(constants.LOGIN_ENDPOINT)
def login_user():
    
#try:

    # Verify JSON Content Type
    if(not request.is_json):
        return {
            constants.ERROR_MESSAGE: constants.ERROR_CONTENT_NOT_JSON
        }, constants.HTTP_BAD_REQUEST_CODE

    user_login_data = request.get_json()

    if(not((constants.EMAIL in user_login_data) and (constants.PASSWORD in user_login_data))):
        return {
            constants.ERROR_MESSAGE: constants.ERROR_MISSING_FIELDS
        }, constants.HTTP_BAD_REQUEST_CODE

    email = user_login_data[constants.EMAIL]
    password = user_login_data[constants.PASSWORD]

    if((not database.email_exists(email)) or (not login.password_matches(email, password))):
        return {
            constants.ERROR_MESSAGE: constants.ERROR_EMAIL_PASSWORD_INCORRECT
        }, constants.HTTP_UNAUTHORIZED_CODE

    user = database.get_user_by_email(email)

    session[constants.USER_ID] = user[constants.USER_ID]

    user.pop(constants.OBJECT_ID)
    user.pop(constants.USER_ID)
    user.pop(constants.PASSWORD)

    return dumps(user), constants.HTTP_OK_CODE

#except:

    return {
        constants.ERROR_MESSAGE: constants.ERROR_LOGIN
    }, constants.HTTP_INTERNAL_ERROR_CODE
        