from flask import Flask
import psycopg2
import time

app = Flask(__name__)
app.config.from_pyfile('settings.py')
while True:
    try:
        conn = psycopg2.connect(host= app.config.get("DATABASE_HOSTNAME") , database = app.config.get("DATABASE_NAME"), user = app.config.get("DATABASE_USERNAME") , password = app.config.get("DATABASE_PASSWORD"))
        cur = conn.cursor()
        print("database connection successfull")
        break
    except Exception as error:
        print  ("error" , error)
        time.sleep(2)

from market import create_tables
from market import routes