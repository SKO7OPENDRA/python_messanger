"""
Что бы я делал без этого сайта:
https://tproger.ru/translations/regular-expression-python/

1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import csv
import re


def get_data():
    c_prod_name = []
    c_name_name = []
    c_code_name = []
    c_type_name = []
    main_data = []

    for i in range(0, 3):
        log_file = open(f'info_{i+1}.txt')
        log_data = log_file.read()

        # производитель
        c_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')     # регулярка
        c_prod_comp = c_prod_reg.findall(log_data)[0].split()[2]    # компилярка
        c_prod_name.append(c_prod_comp)                             # добавлялка

        # система
        c_name_reg = re.compile(r'Windows\s*\S*')
        c_name_comp = c_name_reg.findall(log_data)[0]
        c_name_name.append(c_name_comp)

        # код продукта
        c_code_reg = re.compile(r'Код продукта:\s*\S*')
        c_code_comp = c_code_reg.findall(log_data)[0].split()[2]
        c_code_name.append(c_code_comp)

        # тип системы
        c_type_reg = re.compile(r'Тип системы:\s*\S*')
        c_type_comp = c_type_reg.findall(log_data)[0].split()[2]
        c_type_name.append(c_type_comp)

        print(c_prod_name, '\n', c_name_name, '\n', c_code_name, '\n', c_type_name)

    parameter = ['Изготовитель системы ', ' Название ОС', ' Код продукта', ' Тип системы']
    main_data.append(parameter)

    print(main_data)

    for i in range(0, 3):
        parameter_value = [i + 1,
                           ' ' + c_prod_name[i],
                           ' ' + c_name_name[i],
                           ' ' + c_code_name[i],
                           ' ' + c_type_name[i]]

        # parameter_value.append(f'{i+1}, {c_prod_name[i]}, {c_name_name[i]}, {c_code_name[i]}, {c_type_name[i]}')
        # Строка вставляется с ковычками

        main_data.append(parameter_value)  # помещение в главный список
        # print(main_data)
    return main_data


# запись в файл
def write_to_csv(log_report):
    main_data = get_data()
    with open(log_report, 'w', encoding='utf-8') as f_n:
        file_writer = csv.writer(f_n, delimiter=',')
        for row in main_data:
            file_writer.writerow(row)


# создание файла
write_to_csv('log_report.csv')
