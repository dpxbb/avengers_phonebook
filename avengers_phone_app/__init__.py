from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# Init our database
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app, db)

# Login Config
login_manager = LoginManager(app)
login_manager.login_view = 'login'
from avengers_phone_app import routes, models