# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый тип на кириллице.


import subprocess


for PING_RES in ['yandex.ru', 'youtube.com']:
    PING_LINE = ['ping', PING_RES]
    YA_PING = subprocess.Popen(PING_LINE, stdout=subprocess.PIPE)
    for line in YA_PING.stdout:
        print(line.decode('CP1125').encode('utf-8').decode('utf-8'))


# изначальный код, на 1 строку длиннее

# PING_RES = ['yandex.ru', 'youtube.com']
# for i in PING_RES:
#     PING_LINE = ['ping', i]
#     YA_PING = subprocess.Popen(PING_LINE, stdout=subprocess.PIPE)
#     for line in YA_PING.stdout:
#         print(line.decode('CP1125').encode('utf-8').decode('utf-8'))
