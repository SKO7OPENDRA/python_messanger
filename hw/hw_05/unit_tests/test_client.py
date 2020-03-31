import unittest
from hw_3_1_client import *
import time


class TestClient(unittest.TestCase):
    def test_create_message(self):
        correct_message = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                USER_NAME: DEFAULT_USER_NAME
            }
        }
        message_created = create_presence()
        self.assertEqual(type(message_created), type(correct_message))
        self.assertEqual(message_created[ACTION], correct_message[ACTION])
        self.assertAlmostEqual(message_created[TIME], correct_message[TIME], 3)
        self.assertEqual(message_created[USER], correct_message[USER])

    def create_presence(self):
        self.assertEqual(create_presence('Krepkov')[
                         USER][USER_NAME], 'Krepkov')

    def test_create_presence_exception_too_long(self):
        with self.assertRaises(UsernameToLongError):
            # В скобках 26 символов, потому что ошибка, если больше 25
            create_presence('Toooooooooooooo Long Name!')

    def test_create_presence_exception_wrong_type(self):
        with self.assertRaises(TypeError):
            create_presence(1)

    def test_translate_message_exception_not_dict(self):
        with self.assertRaises(TypeError):
            translate_message('')

    def test_translate_message_exception_no_response(self):
        with self.assertRaises(RCKeyError):
            translate_message({})

    def test_translate_message_exception_response_code_error(self):
        with self.assertRaises(RCLenError):
            translate_message({RESPONSE: 1000})

    def test_translate_message_exception_response_code_not_known(self):
        with self.assertRaises(RCError):
            translate_message({RESPONSE: 404})

    def test_translate_message(self):
        self.assertEqual(translate_message({RESPONSE: OK}), {RESPONSE: OK})


if __name__ == "__main__":
    unittest.main()
