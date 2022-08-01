import random
from array import *
from random import Random

# Challenge 090 #

i = 0
my_list = array('i', [])

while True:
    if i < 5:
        taking_number = int(input("Type in a number between 10 and 20 : "))
        if 10 <= taking_number <= 20:
            my_list.append(taking_number)
            i += 1
        else:
            print("Outside of the range!")
    else:
        print("Thank you!")
        for i in range(0, 5):
            print(my_list[i])
        break

# Challenge 091 #

array_one = [1, 2, 1, 2, 4, 5, 6, 6, 6]
print(array_one)

count_one = int(input("Type a number to count how many seems in the list: "))
print(array_one.count(count_one))

# Challenge 092 #

first_array = array('i', [])
second_array = array('i', [])

for i in range(0, 3):
    first_array.append(int(input("Type in numbers: ")))

for i in range(0, 5):
    second_array.append(random.randint(0, 100))

# To join different two array, extent() method can be used.#
first_array.extend(second_array)

# Sorting is provided by assigning to the new array.#
first_array = sorted(first_array)

for i in range(0, len(first_array)):
    print(first_array[i])

'''for i in range(0, 20):
    print("New Screen!")'''

