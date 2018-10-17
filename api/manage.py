import os
from flask_script import Manager, prompt
from flask_migrate import Migrate, MigrateCommand

from flask_bcrypt import Bcrypt

from globals.globals import app, db
from config.config import Config
from db.models import User


app.config.from_object(Config)


migrate = Migrate(app, db)
manager = Manager(app)
bcrypt = Bcrypt(app)


@manager.command
def create_user():
    """CLI command which prompts for new username, email and password and stores in the database.

    Prompts for new username, email and password to create a new admin account.
    """

    username = prompt(
        'Please enter a username (max length 20 chars)')
    email = prompt(
        'Please enter an email address (max length 120 chars)')
    password = prompt(
        'Please enter a password (max length 128 chars)')

    hash_pw = bcrypt.generate_password_hash(password)

    new_user = User(username=username, email=email, password=hash_pw)
    db.session.add(new_user)
    db.session.commit()


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
