import unittest
from unittest.mock import MagicMock
from unittest import mock, TestCase
from commands.create_user_command import CreateUserCommand, prompt, prompt_pass
from db.models import User
from flask_bcrypt import Bcrypt
from globals.globals import app


class TestCommandCreateUser(TestCase):

    def setUp(self):
        self.command = CreateUserCommand()
        self.bcrypt = Bcrypt(app)

    @mock.patch('commands.create_user_command.CreateUserCommand.hash_password',
                MagicMock(return_value='test'))
    @mock.patch('commands.create_user_command.prompt', MagicMock(return_value='test'))
    @mock.patch('commands.create_user_command.prompt_pass', MagicMock(return_value='test'))
    @mock.patch('commands.create_user_command.db.session.add', MagicMock(return_value=None))
    @mock.patch('commands.create_user_command.db.session.commit', MagicMock(return_value=None))
    def test_command_create_user(self):
        new_user = self.command.run()

        expected_user = User(username='test', email='test', password='test')
        self.assertEqual(new_user.__repr__(), expected_user.__repr__())

    @mock.patch('commands.create_user_command.CreateUserCommand.run',
                MagicMock(return_value=User(username='test', email='test', password=CreateUserCommand().hash_password('test'))))
    def test_command_create_user_hash_password_is_bytes(self):
        new_pw_hashed = self.command.run().password
        self.assertIsInstance(new_pw_hashed, bytes)

    @mock.patch('commands.create_user_command.CreateUserCommand.run')
    def test_command_create_user_hash_password(self, mock_command_run):
        hashed_pw = self.command.hash_password('test')
        mock_command_run.return_value = User(
            username='test', email='test', password=hashed_pw)

        user = mock_command_run()
        self.assertTrue(self.bcrypt.check_password_hash(user.password, 'test'))


if __name__ == '__main__':
    unittest.main()
