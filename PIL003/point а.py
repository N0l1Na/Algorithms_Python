"""

PIL - задача взята с задачника Пильщикова по Паскаль

Task 5.15 page 24
Operators

Вычислить уравнение y = cos(x) + cos(x^2) + cos(x^3) +...+ cos(x^30)

"""

from math import *

x = int(input("x="))
sum = 0
i = 1
while i < 31:
    sum = cos(pow(x, i)) + sum
    i += 1
    print("Сумма=" + str(sum))