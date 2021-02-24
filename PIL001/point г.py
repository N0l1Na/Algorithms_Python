"""

PIL - задача взята с задачника Пильщикова по Паскаль

Task 4.10 page 20
Operators

Даны числа a,b,c ОДЗ: a ≠ 0
Найти вещественные корни уравнения ax^4 + bx^2 + c = 0
Если корней нет - сообщить об этом

"""

from math import *

print("Решаем уравнение ax^4*+bx^2+c=0")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
D = pow(b, 2) - 4*a*c
print("D=" +str(D))
if D < 0:
    print("Корней нет")
elif a == 0:
    print("Ошибка (a≠0) по условию задачи")
elif D == 0:
    y = -b/(2*a)
    if y <0:
        print("Корней нет")
    else:
        x = pow(y, 0.5)
        print("x=" + str(x))
else:
    y2 = (-b + pow(D, 0.5))/(2*a)
    if y2 <0:
        print("x1=Корней нет")
    else:
        x3 = pow(y2, 0.5)
        print("x1=" + str(x3))

    y3 = (-b - pow(D, 0.5))/(2*a)
    if y3 <0:
        print("x2=Корней нет")
    else:
        x3 = pow(y3, 0.5)
        print("x2=" + str(x3))