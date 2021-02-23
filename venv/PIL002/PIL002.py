"""

PIL - задача взята с задачника Пильщикова по Паскаль

Task 5.14 page 24
Operators

Решить уравнение y = sqrt(3+sqrt(6+...+sqrt(96+sqrt(99))))

"""

from math import *

sum = 0
i = 33
while i > 0:
    sum = sqrt(3*i + sum)
    i -= 1
    print("Сумма=" + str(sum))