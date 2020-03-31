import sys
# import json
from socket import *
from common.utilits import get_message, send_message
from common.constants import *
from log_config.server_log_config import SERVER_LOGGER


def main():
    global server
    global client
    server = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        SERVER_LOGGER.warning("Нет адреса, использован стандартный")
        addr = ''

    try:
        port = int(sys.argv[2])
    except IndexError:
        SERVER_LOGGER.warning("Выбран стандарный порт: 7777")
        port = 7777
    except ValueError:
        SERVER_LOGGER.warning("Порт должен быть целым числом")
        sys.exit(0)

    # a.setsockopt(SOL_SOCKET, SO_REUSEADDR, &value, sizeof(value));
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((addr, port))
    server.listen(1)
    while True:
        client, addr = server.accept()
        SERVER_LOGGER.debug("1. Подтверждение")
        message = get_message(client)
        SERVER_LOGGER.debug("2. Получение сообщения")
        print(message)
        SERVER_LOGGER.info('Message: ' + str(message))
        response = server_response(message)
        SERVER_LOGGER.debug("3. Отправка ответа")
        send_message(client, response)
        client.close()


def server_response(message):
    if ACTION in message and \
            message[ACTION] == PRESENCE \
            and TIME in message \
            and isinstance(message[TIME], float):
        SERVER_LOGGER.debug("Ответ от сервера: ОК")
        return {RESPONSE: 200}
    SERVER_LOGGER.warning("Ответ от сервера: ОШИБКА")
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'}


# Спасибо stackoverflow за эту подсказку
if __name__ == '__main__':
    SERVER_LOGGER.info("Сервер запущен")
    try:
        main()
    except Exception as e:
        SERVER_LOGGER.error("Exception: {}".format(str(e)))
    SERVER_LOGGER.info("Сервер остановлен")
