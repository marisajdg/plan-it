# -------------------------------------
# Plan It
# Web Service
# 'authentication_endpoints.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from __main__ import app
from bson.json_util import dumps
from flask import request, session
from database.database import Database
from . import register
from . import login
import constants

# Register User Endpoint
@app.put(constants.Routes.REGISTER_ENDPOINT)
def register_user():

#try:
    
    # Verify JSON Content Type
    if(not request.is_json):
        return {
            constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_CONTENT_NOT_JSON
        }, constants.HttpCodes.HTTP_BAD_REQUEST_CODE

    user_data = request.get_json()

    if(not((constants.Text.USERNAME in user_data) and (constants.Text.EMAIL in user_data) and (constants.Text.PASSWORD in user_data))):
        return {
            constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_MISSING_FIELDS
        }, constants.HttpCodes.HTTP_BAD_REQUEST_CODE

    username = user_data[constants.Text.USERNAME]
    email = user_data[constants.Text.EMAIL]
    password = user_data[constants.Text.PASSWORD]
    
    if(not register.valid_username(username)):
        return {
            constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_INVALID_USERNAME
        }, constants.HttpCodes.HTTP_BAD_REQUEST_CODE

    if(not register.valid_email(email)):
        return {
            constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_INVALID_EMAIL
        }, constants.HttpCodes.HTTP_BAD_REQUEST_CODE

    if(not register.valid_password(password)):
        return {
            constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_INVALID_PASSWORD
        }, constants.HttpCodes.HTTP_BAD_REQUEST_CODE

    if(Database.username_exists(username)):
        return {
            constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_USERNAME_EXISTS
        }, constants.HttpCodes.HTTP_CONFLICT_CODE

    if(Database.email_exists(email)):
        return {
            constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_EMAIL_EXISTS
        }, constants.HttpCodes.HTTP_CONFLICT_CODE

    register.register_user(username, email, password)

    user = Database.get_user_by_email(email)

    session[constants.Text.USER_ID] = user[constants.Text.USER_ID]

    user.pop(constants.Text.OBJECT_ID)
    user.pop(constants.Text.USER_ID)
    user.pop(constants.Text.PASSWORD)

    return dumps(user), constants.HttpCodes.HTTP_CREATED_CODE

#except:

    return {
        constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_REGISTER
    }, constants.HttpCodes.HTTP_INTERNAL_ERROR_CODE

# Login User Endpoint
@app.post(constants.Routes.LOGIN_ENDPOINT)
def login_user():
    
#try:

    # Verify JSON Content Type
    if(not request.is_json):
        return {
            constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_CONTENT_NOT_JSON
        }, constants.HttpCodes.HTTP_BAD_REQUEST_CODE

    user_login_data = request.get_json()

    if(not((constants.Text.EMAIL in user_login_data) and (constants.Text.PASSWORD in user_login_data))):
        return {
            constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_MISSING_FIELDS
        }, constants.HttpCodes.HTTP_BAD_REQUEST_CODE

    email = user_login_data[constants.Text.EMAIL]
    password = user_login_data[constants.Text.PASSWORD]

    if((not Database.email_exists(email)) or (not login.password_matches(email, password))):
        return {
            constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_EMAIL_PASSWORD_INCORRECT
        }, constants.HttpCodes.HTTP_UNAUTHORIZED_CODE

    user = Database.get_user_by_email(email)

    session[constants.Text.USER_ID] = user[constants.Text.USER_ID]

    user.pop(constants.Text.OBJECT_ID)
    user.pop(constants.Text.USER_ID)
    user.pop(constants.Text.PASSWORD)

    return dumps(user), constants.HttpCodes.HTTP_OK_CODE

#except:

    return {
        constants.Errors.ERROR_MESSAGE: constants.Errors.ERROR_LOGIN
    }, constants.HttpCodes.HTTP_INTERNAL_ERROR_CODE
        