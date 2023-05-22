from datetime import datetime
from flask import Flask
from pony.flask import Pony
from pony.orm import Database, Required, Optional
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'fromagerie'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

db = Database()

Pony(app)


