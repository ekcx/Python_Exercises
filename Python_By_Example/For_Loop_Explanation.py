# using for loop in specified value:

# It will be displaying -> 0,1,2,3,4....
# It means that Start from 0 and count 10 different numbers to 10

for i in range(0, 10):
    print(i)

print()

for j in range(5, 10):  # start from 5 and count to 10 at total 5 numbers.
    print(j*j)

# Factorial Calculation.
get_factorial = int(input("Type a factorial number: "))
number = 1

for i in range(2, get_factorial+1):
    number *= i

print(number)



