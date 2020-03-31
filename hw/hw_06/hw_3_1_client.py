import time
import sys
import select
from socket import *    # socket, AF_INET, SOCK_STREAM
from common.errors import UsernameToLongError, RCError, RCLenError, RCKeyError
from common.constants import *
from common.utilits import send_message, get_message
from log_config.client_log_config import CLIENT_LOGGER
from decorator.decorator import log


@log
def main():
    client = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        CLIENT_LOGGER.warning("Нет адреса сервера")
        addr = 'localhost'
    try:
        port = int(sys.argv[2])
    except IndexError:
        CLIENT_LOGGER.warning("Выбран стандарный порт: 7777")
        port = 7777
    except ValueError:
        CLIENT_LOGGER.error("Порт должен быть целым числом")
        client.close()
        sys.exit(0)
    try:
        mode = sys.argv[3]
    except IndexError:
        mode = 'r'

    CLIENT_LOGGER.debug("1. Соединение")
    client.connect((addr, port))
    message = create_presence()
    CLIENT_LOGGER.debug("2. Отправка сообщения")
    send_message(client, message)
    CLIENT_LOGGER.debug("3. Ожидание ответа")
    response = get_message(client)
    response = translate_message(response)
    print(response)
    CLIENT_LOGGER.info('Response: ' + str(response))
    client.close()

@log
def translate_message(response):
    if not isinstance(response, dict):
        CLIENT_LOGGER.error("translate_message Ошибка типа")
        raise TypeError
    if RESPONSE not in response:
        CLIENT_LOGGER.error("translate_message Ошибка ключа")
        raise RCKeyError(RESPONSE)
    code = response[RESPONSE]
    if len(str(code)) != 3:
        CLIENT_LOGGER.error("translate_message Ошибка длинны")
        raise RCLenError(code)
    if code not in RESPONSE_CODES:
        CLIENT_LOGGER.error("translate_message Ошибка кода ответа")
        raise RCError(code)
    return response


@log
def create_presence(user_name=DEFAULT_USER_NAME):
    if not isinstance(user_name, str):
        CLIENT_LOGGER.warning("create_presence Ошибка типа")
        raise TypeError
    if len(user_name) > 25:
        CLIENT_LOGGER.warning("create_presence Длинное имя пользователя")
        raise UsernameToLongError(user_name)
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            USER_NAME: user_name
        }
    }
    return message


def read_messages(client):
    while True:
        message = get_message(client)
        print(message)


def write_messages(client):
    while True:
        message = create_presence()
        CLIENT_LOGGER.debug("Отправка сообщения")
        send_message(client, message)


# Спасибо stackoverflow за эту подсказку
if __name__ == '__main__':
    CLIENT_LOGGER.info("Клиент запощен")
    try:
        main()
    except Exception as e:
        CLIENT_LOGGER.error("Exception: {}".format(str(e)))
    CLIENT_LOGGER.info("Клиент остановлен")
