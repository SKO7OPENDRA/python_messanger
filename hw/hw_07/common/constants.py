import logging

ACCOUNT_NAME = 'account_name'
ACTION = 'action'
DEFAULT_USER_NAME = 'user_name'   # не больше 25 символов
DESTINATION = 'to'
ENCODING = 'utf-8'
ERROR = 'error'
EXIT = 'exit'
MESSAGE = 'message'
MESSAGE_TEXT = 'message_text'
PRESENCE = 'presence'
RESPONSE = 'response'
SENDER = 'from'
TIME = 'time'
USER = 'user'
USER_NAME = 'user_name'
FROM = 'from'
TO = 'to'

ACCEPTED = 202
BASIC_NOTICE = 100
DEFAULT_IP_ADDRESS = '127.0.0.1'
DEFAULT_PORT = 7777
MAX_CONNECTIONS = 5
MAX_PACKAGE_LENGTH = 1024
OK = 200
SERVER_ERROR = 500
WRONG_REQUEST = 400

RESPONSE_CODES = (
    ACCEPTED,
    BASIC_NOTICE,
    OK,
    SERVER_ERROR,
    WRONG_REQUEST
)

RESPONSE_200 = {
    RESPONSE: 200
}
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}

LOGGING_LEVEL = logging.DEBUG