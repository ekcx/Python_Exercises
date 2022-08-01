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
