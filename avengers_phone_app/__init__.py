from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Init our database
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app, db)

from avengers_phone_app import routes, models