import sys
# import json
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from common.utilits import get_message, send_message
from common.constants import *


def server_response(message):
    if ACTION in message and \
            message[ACTION] == PRESENCE and \
            TIME in message and \
            isinstance(message[TIME], float):
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'}


def main():
    global server
    global client
    server = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = '0.0.0.0'

    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Введите целое число')
        sys.exit(0)

    # a.setsockopt(SOL_SOCKET, SO_REUSEADDR, &value, sizeof(value));
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((addr, port))
    server.listen(1)
    while True:
        client, addr = server.accept()
        message = get_message(client)
        print(message)
        response = server_response(message)
        send_message(client, response)
        client.close()


if __name__ == '__main__':
    main()
