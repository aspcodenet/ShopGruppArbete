from areas.products.productPages import productBluePrint
from areas.site.sitePages import siteBluePrint
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate, upgrade
from flask_security import roles_accepted, auth_required, logout_user
from models import db, seedData
from os import environ
import click
from flask.cli import with_appcontext

load_dotenv()

app = Flask(__name__)
# app.config.from_object('config.ConfigDebug')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SECURITY_REGISTERABLE'] = environ.get('SECURITY_REGISTERABLE')
app.config['SECURITY_PASSWORD_SALT'] = environ.get('SECURITY_PASSWORD_SALT')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)
# user_manager.app = app
# user_manager.init_app(app,db,User)

app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)

@click.command('seed-db')
@with_appcontext
def seed_db_command():
    """Seeds the database."""
    seedData(app)
    click.echo('Database seeded.')

app.cli.add_command(seed_db_command)

if __name__  == "__main__":
    app.run()
