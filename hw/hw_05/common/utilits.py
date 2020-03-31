import json
from common.constants import ENCODING

def dict_to_bytes(message_dict):
    if isinstance(message_dict, dict):
        message = json.dumps(message_dict)
        message = message.encode(ENCODING)
        return message
    else:
        raise TypeError


def bytes_to_dict(message_bytes):
    if isinstance(message_bytes, bytes):
        message = message_bytes.decode(ENCODING)
        message = json.loads(message)
        if isinstance(message, dict):
            return message
        else:
            raise TypeError
    else:
        raise TypeError


def send_message(sock, message):
    presence = dict_to_bytes(message)
    sock.send(presence)


def get_message(sock):
    response = sock.recv(1024)
    response = bytes_to_dict(response)
    return response
