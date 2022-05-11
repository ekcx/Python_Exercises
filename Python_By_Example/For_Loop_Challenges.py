# For Loop Challenges
# Challenge 035
get_name = input("Type your name: ")

for i in range(0, 3):
    print(get_name)

# Challenge 036
number = int(input("Type a number:"))

for i in range(0, number):
    print(get_name)

# Challenge 037
for i in range(0, len(get_name)):
    print(get_name[i])

# Challenge 038
number = int(input("Type in a number: "))
for j in range(0, number):
    for i in range(0, len(get_name)):
        print(get_name[i])

# Challenge 039
get_number = int(input("Type a number between 1-12: "))

for i in range(1, 13):
    print(i, "x",  get_number, "=", i * get_number)

# Challenge 040
get_number = int(input("Type a number that's under 50: "))

for i in range(50, get_number-1, -1):
    print(i)

# Challenge 041

summation = 0
number1 = 0

for i in range(0, 5):
    print("Type", i, "th number:")
    number1 = int(input(" "))
    string = input("Add the last number to total? yes or no.")
    if string == "yes":
        summation += number1
    else:
        print("There is no adding number.Total is still", summation)

print(summation)
