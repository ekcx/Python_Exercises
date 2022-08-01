from array import *
from random import *

# Challenge 094 #

one_array = array('i', [2, 2, 3, 4, 5])
print(one_array)
choice = int(input("Type the number that's in the list: "))
helper = True

while helper:
    if choice in one_array:
        print("The index of choice: ", one_array.index(choice))
        helper = False
    else:
        print("The array does not include your choice!")
        choice = int(input("Type the number that's in the list: "))

# Challenge 095 #

