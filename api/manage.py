import os
from flask_script import Manager, prompt
from flask_migrate import Migrate, MigrateCommand

from flask_bcrypt import Bcrypt

from globals.globals import app, db
from config.config import Config
from db.models import User

from commands.create_user_command import CreateUserCommand


app.config.from_object(Config)

manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('create_user', CreateUserCommand)


if __name__ == '__main__':
    manager.run()
