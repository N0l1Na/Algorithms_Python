"""

PIL - задача взята с задачника Пильщикова по Паскаль

Task 4.10 page 20
Operators

Решить f(x), где f(x) =
2ax + |a-1| при a>1,
иначе (e^x/sqrt(1+a^2))-1

"""

from math import *

a = int(input("Введите число a: "))
if a > 0:
    print ("x =", abs(a-1)/(-2*a))
else:
    print ("x =", log(1+pow(a, 2))/2)
