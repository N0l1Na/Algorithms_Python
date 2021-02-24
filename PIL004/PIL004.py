"""

PIL - задача взята с задачника Пильщикова по Паскаль

Task 7.1 page 33
Operators of variants

а) Какие значения могут принимать переменные x,y,t
Допустимы ли присваивания:
   1. x:=весна; 2. y:=x; 3. t:=тепло; 4. y:=t; 5. t:=жарко
б) Вычислить значения выражений:
   1. весна<лето 2. зима<=лето 3. осень<зима

"""

season = ("winter", "spring", "summer", "autumn")
temp = ("warm", "cold", "hot")

# point A
x = season[1]
y = x
t = temp[0]
print(x, y, t)
y = t
t = temp[2]
print(y, t)

# point B
c = [season[1] < season[2], season[0] <= season[2], season[3] < season[0]]
print("Значения =" + str(c))