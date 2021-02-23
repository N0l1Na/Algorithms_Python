"""

PIL - задача взята с задачника Пильщикова по Паскаль

Task 4.1 page 18
Operators

Пункт а) Записать указанное действие в виде одного условного оператора:
y = cos^2(x) при 0<x<2
y = 1 - sin(x^2) иначе

"""

from math import *

x = int(input("Введите число x: "))
if 0 < x < 2:
    print ("y =", pow(cos(x), 2))
else:
    print ("y =", 1 - pow(sin(x), 2))
