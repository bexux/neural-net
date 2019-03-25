import click
from flask.cli import with_appcontext
from flask.cli import AppGroup
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
# make an environment variable
app.config['SECRET_KEY'] = os.environ.get('MTG_SECRET_KEY', __name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


db_cli = AppGroup('database')

@db_cli.command('create')
def create_db():
    db.create_all()
    print('finished creating db')

@db_cli.command('import-cards')
@click.argument('filepath', default='mtgcard.json')
@with_appcontext
def import_cards(filepath='mtgcard.json'):
    from models import upload_some_cards
    upload_some_cards('mtgcard.json')

app.cli.add_command(db_cli)

from flaskapp import routes