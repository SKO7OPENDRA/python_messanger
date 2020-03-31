import sys
import time
from socket import *    # socket, AF_INET, SOCK_STREAM
from common.errors import UsernameToLongError, RCError, RCLenError, RCKeyError
from common.constants import *
from common.utilits import send_message, get_message


def main():
    client = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = 'localhost'
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Введите целое число')
        client.close()
        sys.exit(0)
    client.connect((addr, port))
    message = create_presence()
    send_message(client, message)
    response = get_message(client)
    response = translate_message(response)
    print(response)
    client.close()


def translate_message(response):
    if not isinstance(response, dict):
        raise TypeError
    if RESPONSE not in response:
        raise RCKeyError(RESPONSE)
    code = response[RESPONSE]
    if len(str(code)) != 3:
        raise RCLenError(code)
    if code not in RESPONSE_CODES:
        raise RCError(code)
    return response


def create_presence(user_name=DEFAULT_USER_NAME):
    if not isinstance(user_name, str):
        raise TypeError
    if len(user_name) > 25:
        raise UsernameToLongError(user_name)
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            USER_NAME: user_name
        }
    }
    return message


if __name__ == '__main__':
    main()
