import unittest
import datetime
import jwt
import time

        # self.FAKE_SECRET = b'5\x86\xba\xcajn6\x94\xb7D6i.\xfe\x00\x16OE)\x0b\x1f\x11\x90M'

class TestAuthBlueprint(unittest.TestCase):

    pass
    # def test_encode_auth_token(self):
    #     token = self.auth.encode_auth_token()
    #     self.assertIsInstance(token, bytes)

    
    # def test_decode_auth_token_success(self):
    #     token = self.auth.encode_auth_token()
    #     self.assertTrue(self.auth.decode_auth_token(token) == self.auth.HARDCODED_USER_ID)

    # def test_decode_auth_token_invalid(self):
    #     invalid_token = b'junktokenisinvalid'
    #     self.assertEqual(self.auth.decode_auth_token(invalid_token), self.auth.invalid_token_response)

    # def test_decode_auth_token_expired(self):
    #     token = self.auth.encode_auth_token()
    #     time.sleep(2)

    #     self.assertEqual(self.auth.decode_auth_token(token), self.auth.expired_token_response)

if __name__ == '__main__':
    unittest.main()