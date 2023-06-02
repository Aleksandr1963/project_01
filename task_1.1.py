# Задача 1.1.
from typing import List

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
#my_favorite = my_favorite_songs.split(",") #- это наверно имеется ввиду "переопределять", а так-то гораздо интересней был бы код
# и решением было бы (вывод точно такой же)
#print(my_favorite[0], my_favorite[-1], my_favorite[1], my_favorite[-2])
print(my_favorite_songs[:14], my_favorite_songs[-13:], my_favorite_songs[16:30], my_favorite_songs[-26:-15]) # посложнее
# или
print(my_favorite_songs[0:13])
print(my_favorite_songs[-13:])
print(my_favorite_songs[16:30])
print(my_favorite_songs[-26:-15])