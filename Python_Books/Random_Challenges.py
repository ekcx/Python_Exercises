import random

# Challenge 052
print(random.randint(1, 100))

# Challenge 053
fruit = random.choice(["apple", "pineapple", "strawberry", "cherry", "banana"])
print(fruit)

# Challenge 054
head_tail = random.choice(["head", "tail"])
guess = input("Guess head or tail: ")

if guess == head_tail:
    print("You Win!")
else:
    print("Bad Luck!")
print("The computer selected as", head_tail)

# Challenge 055
number = random.randint(1, 5)
count = 0

# Challenge 056 - 057

number_int = random.randint(1, 10)
guess = 0
count = 0

while True:
    if number != guess:
        guess = int(input("Guess an integer: "))
        if guess < number:
            print("Too Low")
        elif guess > number:
            print("Too High")
        count += 1
    else:
        print("It was the picked number!")
        print("You've tried", count, "times.")
        break

# Challenge 058

summation = 0

for i in range(1, 6):
    number = random.randint(1, 5)
    number1 = random.randint(1, 5)

    print("Answer", number, "+", number1, "= :")
    answer = int(input(""))
    if answer == (number + number1):
        summation += 1
    else:
        summation = summation
print("Your grade is", summation, "out of 5")

# Challenge 059

colours = ["red", "black", "green", "blue", "purple"]
guess = colours[random.randint(0, 5)]
for i in range(0, 5):
    print(colours[i])
print("These are the colours.Pick one!")
colour_guess = ""

while colour_guess != guess:

    colour_guess = input("Enter colour:")

    if guess == colour_guess:
        print("Well done")
    else:
        print("I bet you are", guess, "with envy")

