"""

PIL - задача взята с задачника Пильщикова по Паскаль

Task 5.15 page 24
Operators

Вычислить уравнение y = 1! + 2! + 3! +...+ n! (n>1)

"""

n = int(input("n="))
total = 0
i = 1

if n <= 1:
    print("Error: #1 N is less or equal 1")
    exit(-1)

while i < n+1:
    z = 1 + i
    fact = 1

    # function of factorial
    for l in range(1, z+1):
        fact = fact * l

    total = fact + total
    i += 1
    print("Сумма=" + str(total))