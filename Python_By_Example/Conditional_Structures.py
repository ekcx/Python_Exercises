# challenge 012
number1 = int(input("Please enter first integer: "))
number2 = int(input("Please enter second integer: "))

if number1 > number2:
    print(number2)
    print(number1)
else:
    print(number1)
    print(number2)

# challenge 013
number = int(input("Please enter a number that is under 20: "))

if number >= 20:
    print("Too high")
else:
    print("Thank You!")

# challenge 014

number = int(input("Type an integer: "))

if 10 <= number <= 20:
    print("Thank you!")
else:
    print("Incorrect Answer!")

# challenge 015

string = input("What is your fav. color?")

if string == "red" or string == "Red" or string == "RED":
    print("I like red, too.")
else:
    print("I don't like", string, "I prefer red.")

# challenge 016

string = input("Is the weather rainy?")
string = str.lower(string)

if string == "yes":
    string = input("Is the weather windy?")
    string = str.lower(string)
    if string == "yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day!")

# challenge 017

age = int(input("Your age: "))

if age >= 18:
    print("You can vote!")
elif age == 17:
    print("You can learn to drive.")
elif age == 16:
    print("You can buy a lottery ticket.")
else:
    print("You can go Trick-or-Treating.")

# Challenge 018

numbeer = int(input("The Number: "))

if numbeer < 10:
    print("Too low")
elif 10 <= numbeer <= 20:
    print("Correct!")
else:
    print("Too High!")

# Challenge 019

thank_you = int(input("Type 1,2,3 or else: "))

if thank_you == 1:
    print("Thank you.")
elif thank_you == 2:
    print("Well Done.")
elif thank_you == 3:
    print("Correct!")
else:
    print("Error Message!")
