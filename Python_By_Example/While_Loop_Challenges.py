# Explanation of While Loop

print("Till the total is equal 100,")
total = 0
while total < 100:
    num = int(input("Enter a number: "))
    total = total + num

print("The total is", total)

# Challenge 045

total = 0
int_number = 0

while total <= 50:
    number = int(input("Type a number: "))
    total += number
    int_number += 1

print(total)
print("The number of integer: ", int_number)

# Challenge 046

input_int = int(input("Please type a number: "))

while input_int > 5:
    input_int = int(input("Please type a number: "))

print("The last number you entered was a", input_int)

# Challenge 047

summation = 0
get_int = int(input("Please enter first number: "))
summation += get_int
get_int = int(input("Please enter second number: "))
summation += get_int
answer = ""

while True:
    answer = input("Do you want to add the another number?")
    if answer == "y":
        get_int = int(input("Type another number: "))
        summation += get_int
    else:
        break

print(summation)

# Challenge 048

name_number = 0

while True:
    party_name = input("Please type in a name to invite for the party: (no to exit)")
    print(party_name, "has now been invited.")
    name_number += 1
    if party_name == "no":
        print(name_number, "people has been invited.")
        break

# Challenge 049

copnum = 50
guess = 0
count = 0

while copnum != guess:
    guess = int(input("Please type in a number: "))
    count += 1
    if guess > copnum:
        print("Too high")
    elif guess == copnum:
        print("Well done,you took", count, "attempts.")
    else:
        print("Too Low")


while True:
    number_int = int(input("Type in a number: "))
    if number_int <= 10:
        print("Too Low")
    elif number_int >= 20:
        print("Too High")
    else:
        print("Thank You!")
        break

num = int(input("Enter a bottles number: "))

while num != 0:
    print("There are", num, "green bottles hanging on the wall,", num,
          "green bottles hanging on the wall,and if 1 green bottle should accidentally fall")
    print("How many green bottles will be hanging on the wall?")
    fall = int(input(":"))

    if (num - 1) == fall:
        num = num - 1
        print("There will be", num, "green bottles hanging on the wall.")
    elif (num - 1) != 0:
        print("No, try again!")
    else:
        print("There are no more green bottles hanging on the wall.")

