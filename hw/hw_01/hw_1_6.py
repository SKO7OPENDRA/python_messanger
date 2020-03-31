# Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор»
# Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

F_N = open('test_file.txt', 'w', encoding='utf-8')
F_N.write('сетевое программирование сокет декоратор')
F_N.close()
print(type(F_N))

with open('test_file.txt', encoding='utf-8') as F_N:
    for el_str in F_N:
        print(el_str, end="")