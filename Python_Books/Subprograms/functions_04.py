# Challenge 0120

# Displaying two menu to the user
# 1) Addition
# 2) Subtraction
# Enter 1 or 2
import random

print("1) Addition\n")
print("2) Subtraction\n")
choosen = int(input("Enter 1 or 2: "))


def rand_sum():
    first = random.randint(5, 20)
    second = random.randint(5, 20)
    print(f"First and second number: {first} and {second}")
    correct_answer = first + second
    user_answer = int(input("Add them together: "))
    print(f"Your answer is: {user_answer}")
    print(f"The correct answer is: {correct_answer}\n")
    sum_answer = (user_answer, correct_answer)
    return sum_answer


def rand_subt():
    first = random.randint(25, 50)
    second = random.randint(1, 25)
    print(f"First and second number: {first} and {second}")
    correct_answer = first - second
    user_answer = int(input("Minus them together: "))
    print(f"Your answer is: {user_answer}")
    print(f"Your answer is: {correct_answer}")
    subt_answer = (user_answer, correct_answer)
    return subt_answer


# def check(user_answer, correct_answer):
#     if user_answer == correct_answer:
#         print("This is Great!")
#     else:
#         print("Not correct. It is the answer is", correct_answer)


if choosen == 1:
    rand_sum()
elif choosen == 2:
    rand_subt()
else:
    print("The suitable message! :)")


