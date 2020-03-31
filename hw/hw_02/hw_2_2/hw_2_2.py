"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

# {
#     "orders": [
#         {
#             "item": "printer",
#             "quantity": "10",
#             "price": "6700",
#             "buyer": "Ivanov I.I.",
#             "date": "24.09.2017"
#         },
#         {
#             "item": "scaner",
#             "quantity": "20",
#             "price": "10000",
#             "buyer": "Petrov P.P.",
#             "date": "11.01.2018"
#         }
#     ]
# }

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json


def read_orders_from_json():
    with open('orders.json', 'r', encoding='utf-8') as f_i:
        orders = json.load(f_i)
        return orders


def write_order_to_json(orders, item, quantity, price, buyer, date):
    orders_data = {"item": item,
                   "quantity": quantity,
                   "price": price,
                   "buyer": buyer,
                   "date": date
                   }
    orders["orders"].append(orders_data)

    with open('orders.json', 'w', encoding='utf-8') as f_o:
        f_o.write(json.dumps(orders, indent=4))


orders_list = read_orders_from_json()
write_order_to_json(orders_list, 'order 1', 10, 5000, 'Ivanov', '01.01.2001')
write_order_to_json(orders_list, 'order 2', 20, 10000, 'Petrov', '02.02.2002')
write_order_to_json(orders_list, 'order 3', 15, 15000, 'Sidorov', '03.03.2003')
write_order_to_json(orders_list, 'order 4', 20, 20000, 'Kharitonov', '04.04.2004')