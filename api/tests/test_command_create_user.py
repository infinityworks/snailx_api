import unittest
from unittest.mock import MagicMock, Mock
from unittest import mock, TestCase
from commands.create_user_command import CreateUserCommand
from db.models import User


class TestCommandCreateUser(TestCase):

    def setUp(self):
        self.command = CreateUserCommand()

    @mock.patch('commands.create_user_command.CreateUserCommand.run',
                MagicMock(return_value=User(username='test', email='test', password='test')))
    @mock.patch('commands.create_user_command.CreateUserCommand.hash_password',
                MagicMock(return_value='test'))
    def test_command_create_user(self):
        new_user = self.command.run()
        expected_user = User(username='test', email='test', password='test')
        self.assertEqual(new_user.__repr__(), expected_user.__repr__())

    @mock.patch('commands.create_user_command.CreateUserCommand.run',
                MagicMock(return_value=User(username='test', email='test', password=CreateUserCommand().hash_password('test'))))
    def test_command_create_user_hash_password(self):
        new_pw_hashed = self.command.run().password
        self.assertIsInstance(new_pw_hashed, bytes)


if __name__ == '__main__':
    unittest.main()
