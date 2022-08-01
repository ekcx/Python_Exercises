import random
from array import *
from random import Random

nums = array('i', [45, 324, 654, 45, 264])
print(nums)

for i in nums:
    print(i)

newValue = int(input("Enter number: "))
nums.append(newValue)

# it reverses the order of the array.
nums.reverse()
for i in nums:
    print(i)

# This method is sorting in ascending order.

nums = sorted(nums)
print(nums)

nums.pop()
print(nums)

# declaring an integer array #
my_array = array('i', [])

# specifying the size of the list #
length = int(input("Type the limit: "))

# adding the numbers to the nums until to reach the size #
for i in range(0, length):
    number = int(input("Type a number that will be adding to the list: "))
    my_array.append(number)
nums.extend(my_array)
print(nums)

# in here, we are typing the number itself to REMOVE. Not index!!!! #
GetRid = int(input("Type the number of will be removed element: "))
nums.remove(GetRid)
print(nums)

print(nums.count(45))


# Challenge 088 #

list = array('i', [])

for i in range(0, 5):
    list_number = int(input("Type in a number: "))
    list.append(list_number)
list = sorted(list)
print(list)

# Challenge 089 #

random_list = array('i', [])
for i in range(0, 5):
    random_list.append(int(random.randint(0, 100)))
    print(random_list[i])

