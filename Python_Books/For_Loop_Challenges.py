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
name1 = input("Type your name: ")
number2 = int(input("Type a number: "))

if number2 < 10:
    for i in range(0, number2):
        print(name1)
else:
    for i in range(0, 2):
        print("Too High!")


# Challenge 042

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

# Challenge 043

up_down = input("Type up or down: ")

if up_down == "up":
    number = int(input("Type the number: "))
    for i in range(1, number+1):
        print(i)
elif up_down == "down":
    number = int(input("Type the number below 20: "))
    for i in range(20, number-1, -1):
        print(i)
else:
    print("I don't understand.")

# Challenge 044

invited_number = int(input("How many people invented to the party? "))

if invited_number < 10:
    for i in range(0, invited_number):
        get_name = input("Type an invited name: ")
        print(get_name, "has been invited to the party.")
else:
    print("Too many people!")