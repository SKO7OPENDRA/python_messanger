"""
Схема сервера:
ss = socket() # создание сокета сервера
ss.bind()  # привязка сокета к адресу
ss.listen()  # прослушивание запросов на соединение
  inf_loop:  # бесконечный цикл сервера
    cs = ss.accept()  # прием клиентского запроса на установление соединения
      comm_loop:  # цикл связи
        cs.recv() / cs.send()  # обмен данными
    cs.close()  # закрытие сокета клиента
ss.close()  # закрытие сокета сервера (необязательно)


Функции сервера: принимает сообщение клиента;
                 формирует ответ клиенту;
                 отправляет ответ клиенту;
имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""
from socket import socket, AF_INET, SOCK_STREAM
import json
import argparse


def main():     # голова
    args = parse_args()
    port = args.port
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    print(f"Запущено прослушивание порта {str(port)}")
    while True:
        server_communicate(s)


def server_response(client_msg, client):  # ответ от сервера
    json_resp = {}
    if client_msg["action"] == 'presence':
        json_resp = {
            "response": 200,
            "alert": "Подтрерждаю"
        }
    elif client_msg["action"] == 'msg':
        json_resp = {
            "response": 200,
            "alert": "Сообщение отправлено пользователю " + client_msg["to"]
        }
    msg = json.dumps(json_resp)
    client.send(msg.encode('utf-8'))
    client.close()


def input_message(client, addr):
    data = client.recv(1024)
    print("Сообщение", data.decode('utf-8'), ", было отправлено клиентом: %s" % str(addr))
    json_mess = json.loads(data.decode('utf-8'))
    return json_mess


def server_communicate(s: socket):
    client, addr = s.accept()
    print(f"Получен запрос на соединение от {str(addr)}")
    msg_from_user = input_message(client, addr)
    server_response(msg_from_user, client)


def parse_args():
    parser = argparse.ArgumentParser(description='Server App')
    parser.add_argument(
        "-p",
        action="store",
        dest="port",
        type=int,
        default=7777)
    parser.add_argument(
        "-a",
        action="store",
        dest="addr",
        type=str,
        default='0.0.0.0')
    return parser.parse_args()


if __name__ == '__main__':
    main()