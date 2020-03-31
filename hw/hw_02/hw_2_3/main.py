"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
# write_order_to_json(orders_list, 'order 1', 10, 5000, 'Ivanov', '01.01.2001')
# write_order_to_json(orders_list, 'order 2', 20, 10000, 'Petrov', '02.02.2002')
# write_order_to_json(orders_list, 'order 3', 15, 15000, 'Sidorov', '03.03.2003')
# write_order_to_json(orders_list, 'order 4', 20, 20000, 'Kharitonov', '04.04.2004')

import yaml

# Словарь в списке с указанием ключей
key_1 = ['order 1', 'order 2', 'order 3', 'order 4']
key_2 = 10
key_3 = {'order 1': '5000₽', 'order 2': '10000₽', 'order 3': '15000₽', 'order 4': '20000₽'}

key_to_yaml = {'key_1': key_1, 'key_2': key_2, 'key3': key_3}
yaml_data = yaml.dump(key_to_yaml, allow_unicode=True, default_flow_style=False)

# запись в файл
with open('file.yaml', 'w', encoding='utf-8') as f_i:
    f_i.write(yaml_data)

# чтение из файла
with open('file.yaml', 'r', encoding='utf-8') as f_o:
    data_o = yaml.load(f_o, Loader=yaml.FullLoader)

# сравнение файлов
if data_o == key_to_yaml:
    print("Evenly")
else:
    print("Different")

# архивирование файлов