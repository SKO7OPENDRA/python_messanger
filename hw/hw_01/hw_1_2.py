# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое
# и длину соответствующих переменных.

# в байтовом типе без преобразования

FIRST_STR = b'class'
SECOND_STR = b'function'
THIRD_STR = b'method'

# и определить тип

print(type(FIRST_STR))
print(type(SECOND_STR))
print(type(THIRD_STR))

# и длину соответствующих переменных

print(FIRST_STR, SECOND_STR, THIRD_STR)
print(len(FIRST_STR), len(SECOND_STR), len(THIRD_STR))
