"""

PIL - задача взята с задачника Пильщикова по Паскаль

Task 4.1 page 18
Operators

Пункт д) max(x,y) при x < 0, иначе min(x,y)

"""

x = int(input("x2=")); y = int(input("y2="))
if x < 0:
    print ("z =", max(x, y))
else:
    print ("z =", min(x, y))