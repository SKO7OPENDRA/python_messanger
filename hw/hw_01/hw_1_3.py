#3. Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе.

for s in ['attribute', 'класс', 'функция', 'type']:
    try:
        print(s, type(s), s.encode('ascii'), 'да')
    except:
        print(s, type(s), 'нет')