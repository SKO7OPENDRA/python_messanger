'''
Схема клиента:
cs = socket()  # создание сокета клиента
cs.connect()  # попытка установить соединение с сервером
comm_loop:  # цикл связи
    cs.send()/cs.recv  # прием передача данных
cs.close()
'''

# Функции клиента: сформировать presence-сообщение;
#                  отправить сообщение серверу;
#                  получить ответ сервера;
#                  разобрать сообщение сервера;
# параметры командной строки скрипта client.py <addr> [<port>]:
# addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777.


from socket import *
import argparse
import json


def main():     # голова
    args = parse_args()
    port = args.port
    host = args.addr
    msg = json.dumps(presence("Client", "Connection complete"))
    communicate(msg, host, port)
    msg = json.dumps(message_from_user("Krepkov"))
    communicate(msg, host, port)


def message_from_user(from_user):  # Сообщение от пользователя
    to_user = input(u"Введите адресата:")   # адресат
    msg = input(u"Введите текст:")  # сообщение
    return {
        "action": "msg",
        "to": to_user,
        "from": from_user,
        "encoding": "utf-8",
        "Message": msg
    }


def send_message(msg, s):  # отправка сообщения
    s.send(msg.encode('utf-8'))
    print(f"*! NEW Message: {msg}")


def parse_message(str1):  # разобрать сообщение сервера
    try:
        serv_message = json.loads(str1.decode('utf-8'))
        if serv_message["response"] in (100, 101, 200, 201, 202):
            print("Сообщение доставлено на сервер, код возврата ",
                  serv_message["response"], serv_message["alert"])
    except json.decoder.JSONDecodeError:
        print("Сообщение от сервера не распознано", str1)


def presence(username, status):  # сформировать presence-сообщение
    return {
        "action": "presence",
        "type": "status",
        "user": {
            "account_name": username,
            "status": status
        }
    }


def get_response(s):  # получить ответ сервера
    data = s.recv(1024)
    parse_message(data)


def communicate(msg, host, port):   # соединение с портом и отправка сообщения
    print(f"Попытка соединения с {host} по порту {port}")
    my_socket = socket(AF_INET, SOCK_STREAM)
    try:
        my_socket.connect((host, port))
    except ConnectionRefusedError:
        print(f"Сервер {host} недоступен по порту {port}")
    send_message(msg, my_socket)
    my_socket.close()


# получить и обработать параметры командной строки
def parse_args():
    parser = argparse.ArgumentParser(description='Client App')
    parser.add_argument(
        "-a",
        action="store",
        dest="addr",
        type=str,
        default='localhost',
        help="enter IP address, default is localhost")
    parser.add_argument(
        "-p",
        action="store",
        dest="port",
        type=int,
        default=7777,
        help="enter port number, default is 7777")
    return parser.parse_args()


if __name__ == '__main__':
    main()