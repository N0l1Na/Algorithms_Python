"""

PIL - The exercise is taken from the Pilshchikov's Pascal problem book

Task 8.9 page 40
Regular types: vectors

Assign to each element year[i] the name of this day of the week,
which falls on the i-th day of the non-leap year,
if it is known that January 1 is Wednesday

"""

print_day = (int(input("Number of the day in the year = ")) - 1)
day_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
list_of_days_in_year = list(range(1, 366))

if not (0 < print_day < 366):
    print("Please enter the correct non-leap year number (from 1 to 365)")
    quit(-1)

# The function that outputs Wednesday
if list_of_days_in_year[print_day] % 7 == 1:
    print(day_of_week[2])
# The function that outputs Thursday.
elif list_of_days_in_year[print_day] % 7 == 2:
    print(day_of_week[3])
# The function that outputs Friday.
elif list_of_days_in_year[print_day] % 7 == 3:
    print(day_of_week[4])
# The function that outputs Saturday.
elif list_of_days_in_year[print_day] % 7 == 4:
    print(day_of_week[5])
# The function that outputs Sunday.
elif list_of_days_in_year[print_day] % 7 == 5:
    print(day_of_week[6])
# The function that outputs Monday.
elif list_of_days_in_year[print_day] % 7 == 6:
    print(day_of_week[0])
# The function that outputs Tuesday.
elif list_of_days_in_year[print_day] % 7 == 0:
    print(day_of_week[1])
