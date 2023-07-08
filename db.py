import os

import mysql.connector
from dotenv import load_dotenv

# Loading variable from env file
load_dotenv()

# Creating a database connection
mydb = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE')
)
