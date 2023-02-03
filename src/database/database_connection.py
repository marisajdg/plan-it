# -------------------------------------
# Plan It
# Web Service
# 'database_connection.py'
# Contact: planit.app.dev@gmail.com
# -------------------------------------

from dotenv import load_dotenv
from pathlib import Path
import constants
import pymongo
import os

env_path = Path('../../.env')

load_dotenv(dotenv_path=env_path)

# Database connection
database_client = pymongo.MongoClient(str(os.getenv(constants.DB_CONNECTION_URI)))
