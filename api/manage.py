from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

from globals.globals import app, db
from config.config import Config

from commands.create_user_command import CreateUserCommand


app.config.from_object(Config)

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('create_user', CreateUserCommand)


if __name__ == '__main__':
    manager.run()
