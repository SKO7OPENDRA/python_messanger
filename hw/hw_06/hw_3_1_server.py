import sys
# import json
from socket import *
from common.utilits import get_message, send_message
from common.constants import *
from log_config.server_log_config import SERVER_LOGGER
from decorator.decorator import log


@log
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
    SERVER_LOGGER.debug("Starting connection...")
    server.bind((addr, port))
    server.listen(15)
    server.settimeout(0.2)
    clients = []
    while True:
        
        client, addr = server.accept()




@log
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


def read_requests(r_clients, all_clients):
    messages = []
    for sock in r_clients:
        try:
            message = get_message(sock)
            messages.append(message)
        except BaseException:
            print(
                'Client {} {} disconnected'.format(
                    sock.fileno(),
                    sock.getpeername()))
            all_clients.remove(sock)

    return messages


def write_responses(messages, w_clients, all_clients):
    for sock in w_clients:
        for message in messages:
            try:
                response = server_response(message)
                send_message(sock, response)
            except:
                print('Client {} {} disconnected'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


# Спасибо stackoverflow за эту подсказку
if __name__ == '__main__':
    SERVER_LOGGER.info("Сервер запущен")
    try:
        main()
    except Exception as e:
        SERVER_LOGGER.error("Exception: {}".format(str(e)))
    SERVER_LOGGER.info("Сервер остановлен")
