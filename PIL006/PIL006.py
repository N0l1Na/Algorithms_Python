"""

PIL - The exercise is taken from the Pilshchikov's Pascal problem book

Task 8.7 page 40
Regular types: vectors

Using the Gender and Height arrays, determine:
a) The name of the tallest man
b) The average height of women

Creator Mikhail Mun

"""

import random

array = []
total_height_women = 0
amount_women = 0
max_height = None
names = ("Valeria", "Gena", "Eugene", "Nikola", "Maria", "Nina", "Sasha", "Tanya", "Fedor", "Shura")
genders = ("woman", "man", "man", "man", "woman", "woman", "woman", "woman", "man", "woman")
for i in range(0, 10):
    # gender determination
    output_gender = print(names[i] + " " + str(genders[i]))

    # height determination
    generate_random_height = random.randrange(140, 201)
    output_age = print(names[i] + " (" + str(generate_random_height) + "sm)")

    # max the height of the man
    if genders[i] == "man":

        # add element in the list
        array.append(str(generate_random_height))

        # find max element of the list
        max_height = max(array)

    # average function
    elif genders[i] == "woman":
        amount_women = amount_women + 1
        total_height_women = total_height_women + generate_random_height

print("Max the height of the man " + str(max_height))
print("Average women= " + str(total_height_women / amount_women))