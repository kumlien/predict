import click
from flask.cli import with_appcontext
from predict import db
from predict.models import User
from predict import create_app


#Set the FLASK_APP env var for this to work
@click.command(name='db-init-data')
@with_appcontext
def db_init_data():
    """Init db with some data"""
    print("create all...")
    db.create_all()


if __name__ == '__main__':
    db_init_data()
