"""

PIL - задача взята с задачника Пильщикова по Паскаль

Task 4.10 page 20
Operators

Дано число x, необходимо напечатать в порядке возрастания:
chx, 1+|x|, (1+x^2)^x

"""

from math import *

x = int(input("Введите число x: "))
f = [cosh(x), 1+abs(x), pow((1+pow(x, 2)), x)]
f.sort()
print(f)
