# Задача 1.2.
import datetime

# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

# my_favorite_songs = [
#     ['Waste a Moment', 3.03],
#     ['New Salvation', 4.02],
#     ['Staying\' Alive', 3.40],
#     ['Out of Touch', 3.03],
#     ['A Sorta Fairytale', 5.28],
#     ['Easy', 4.15],
#     ['Beautiful Day', 4.04],
#     ['Nowhere to Run', 2.58],
#     ['In This World', 4.02],
# ]
#
# import random
#
# first_song = random.choice(my_favorite_songs)
#
# time_first_song = first_song[1]
# #print(time_first_song)# - промежуточная проверка
#
# my_favorite_songs.remove(first_song)# удаление первой выбранной песни
# # print(my_favorite_songs)# промежуточная проверка списка
# second_song = random.choice(my_favorite_songs)
# #print(second_song)
# time_second_song = second_song[1]
# print(time_second_song)
# my_favorite_songs.remove(second_song)# удаление  второй выбранной песни
# third_song = random.choice(my_favorite_songs)
# time_third_song = third_song[1]
# #print(time_third_song)# - проверка
#
#
# from datetime import timedelta, datetime
# a = timedelta(minutes = int(time_first_song), seconds = (time_first_song - int(time_first_song))*100)
# b = timedelta(minutes = int(time_second_song), seconds = (time_second_song - int(time_second_song))*100)
# c = timedelta(minutes = int(time_third_song), seconds = (time_third_song - int(time_third_song))*100)
# # print(a) # проверка
# # print(b) # проверка
# # print(c) # проверка
# z = a + b + c
#
# print("Три песни звучат" , z , "минут")
#
#

# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

import random
# Выбираем первую песню
first_song = random.choice(list(my_favorite_songs_dict))
# print(first_song)
# Определяем время звучания первой песни
time_first_song = my_favorite_songs_dict[first_song]
# print(time_first_song)
# Выводим первую песню из списка
del my_favorite_songs_dict[first_song]
# print(my_favorite_songs_dict)
# Определяем рандомно вторую песню
second_song = random.choice(list(my_favorite_songs_dict))
# print(second_song)
# Определяем время звучания второй песни
time_second_song = my_favorite_songs_dict[second_song]
# print(time_second_song)
# Выводим из списка вторую песню
del my_favorite_songs_dict[second_song]
# print(my_favorite_songs_dict)
# Определяем рандомно третью песню
third_song = random.choice(list(my_favorite_songs_dict))
# print(third_song)
# Определяем время звучания третьей песни
time_third_song = my_favorite_songs_dict[third_song]
# print(time_third_song)

# Переводим время звучания во временной формат

from datetime import timedelta
a = timedelta(minutes = int(time_first_song), seconds = (time_first_song - int(time_first_song))*100)
b = timedelta(minutes = int(time_second_song), seconds = (time_second_song - int(time_second_song))*100)
c = timedelta(minutes = int(time_third_song), seconds = (time_third_song - int(time_third_song))*100)
# print(a) # проверка
# print(b) # проверка
# print(c) # проверка

# Проводим сложение во временном формате
z = a + b + c
# Выводим ответ задачи
print("Три песни звучат" , z , "минут")
