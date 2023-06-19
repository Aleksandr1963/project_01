# Задача 2.4.

# Пункт B.
# Удалите восклицательный знак из конца строки.
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# Решение
def remove_last_em(s):
    #s = input('Введите текст:')
    #print(s)
    if s[-1] == '!':
        bc = s[:-1]
    else:
        bc = s
    return bc
s = "Hi!"
print(f'"{remove_last_em(s)}"')
s = "Hi!!!"
print(f'"{remove_last_em(s)}"')
s = "!Hi"
print(f'"{remove_last_em(s)}"')
