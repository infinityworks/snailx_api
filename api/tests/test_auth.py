import unittest
import datetime
import jwt

class MockAuth():

    def __init__(self):
        self.HARDCODED_USER_ID = 1
        self.FAKE_SECRET = b'5\x86\xba\xcajn6\x94\xb7D6i.\xfe\x00\x16OE)\x0b\x1f\x11\x90M'

    def encode_auth_token(self):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
            'iat': datetime.datetime.utcnow(),
            'sub': self.HARDCODED_USER_ID
        }

        # fake secret key
        token = jwt.encode(
            payload,
            self.FAKE_SECRET,
            algorithm='HS256'
        )
        return token

    def decode_auth_token(self, auth_token):
        try:
            payload = jwt.decode(auth_token, self.FAKE_SECRET)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class TestAuthBlueprint(unittest.TestCase):

    def setUp(self):
        self.auth = MockAuth()

    def test_encode_auth_token(self):
        token = self.auth.encode_auth_token()
        self.assertIsInstance(token, bytes)

    def test_decode_auth_token(self):
        token = self.auth.encode_auth_token()
        self.assertTrue(self.auth.decode_auth_token(token) == self.auth.HARDCODED_USER_ID)

if __name__ == '__main__':
    unittest.main()