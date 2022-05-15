# Random Numbers and Random Functions

import random

num = random.random()
print(num*100)
print(num*10)
print(num*2)

num = random.randint(0, 9)
print(num)
num = random.randint(5, 15)
print(num)
num = random.randint(20, 30)
print(num)

num1 = random.randint(0, 1000)
num2 = random.randint(0, 1000)
newrand = num1 / num2
print(newrand)

num = random.randrange(0, 100, 5)
print(num)
# picks a random number between 0 and 100 in 5x

colour = random.choice(["red", "black", "green", 5, 19, "purple"])
# Remember! the string data type needs to include speech marks but numeric data does not.
print(colour)