"""

PIL - задача взята с задачника Пильщикова по Паскаль

Task 4.1 page 18
Operators

Пункт б) Переменной x присвоить корень уравнения:
arcsin(1+ln(x))=a

"""

from math import *

x = int(input("Введите число x1: "))
print ("a =", sqrt(asin(1+log(x))))