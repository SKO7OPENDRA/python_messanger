import unittest

from hw_3_1_server import *
import time


class TestClient(unittest.TestCase):
    def test_message_response(self):
        correct_message = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                USER_NAME: DEFAULT_USER_NAME
            }
        }
        self.assertEqual(server_response(correct_message), {RESPONSE: 200})

    def test_message_response_incorrect(self):
        incorrect_message = {
        }
        self.assertEqual(
            server_response(incorrect_message), {
                RESPONSE: 400, ERROR: 'Bad Request'})
