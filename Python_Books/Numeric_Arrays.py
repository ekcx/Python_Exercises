from array import *

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
