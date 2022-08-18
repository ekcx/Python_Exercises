# Challenge 119
import random


def pick_numbers():
    first = int(input("Type a first number: "))
    second = int(input("Type a second number: "))
    comp_num = random.randint(first, second)
    return comp_num


def guess_number():
    guess = int(input("I am thinking of a number..."))
    return guess


def main():

    first = pick_numbers()
    second = guess_number()
    i = True

    while i:

        if first == second:
            print("Correct! You win!")
            i = False
        else:
            if first < second:
                print("Your guess is too high. Try again: ")
                second = guess_number()
            else:
                print("Your guess is too low. Try again: ")
                second = guess_number()



main()