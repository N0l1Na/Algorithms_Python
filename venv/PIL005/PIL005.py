"""

PIL - The exercise is taken from the Pilshchikov's Pascal problem book

Task 7.13 page 36
Operators of variants

Define season-the season that the month-month falls on
If January is the month[0]

Creator Mikhail Mun

"""

i = int(input("введите номер месяца  "))
season = ("winter", "spring", "summer", "autumn")
month = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
a = month[i]
if a == month[11 or 0 or 1]:
    print(season[0])
elif a == month[2 or 3 or 4]:
    print(season[1])
elif a == month[5 or 6 or 7]:
    print(season[2])
elif a == month[8 or 9 or 10]:
    print(season[3])
else:
    print("Error")