from flask_script import Command, prompt, prompt_pass
from flask_bcrypt import Bcrypt
from globals.globals import db, app
from db.models import User


class CreateUserCommand(Command):
    """CLI command which prompts for new username, email and password and stores in the database.

    Prompts for new username, email and password to create a new admin account.
    """

    def run(self):
        username = prompt(
            'Please enter a username (max length 20 chars)')
        email = prompt(
            'Please enter an email address (max length 120 chars)')
        password = prompt_pass(
            'Please enter a password (max length 128 chars)')

        hash_pw = Bcrypt(app).generate_password_hash(password)
        new_user = User(username=username, email=email, password=hash_pw)

        db.session.add(new_user)
        db.session.commit()
