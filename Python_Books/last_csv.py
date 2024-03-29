import csv
import random

# Challenge 116

book_file = open("Books.csv", "w")
book_file.write("To Kill A Mockingbird, Harper Lee, 1960\n")
book_file.write("A Brief History of Time, Stephen Hawking, 1988\n")
book_file.write("The Great Gatsby, F. Scott Fitzgerald, 1992\n")
book_file.write("The Man Who Mistook His Wife for a Hat, Oliver Scaks, 1985\n")
book_file.write("Pride and Prejudice, Jane Austen, 1813")
book_file.close()

list_of_book = list(open("Books.csv", "r"))
first_list = []     # Declaration of the empty list.

i = 0
for row in list_of_book:
    first_list.append(row)
    print(str(i) + " " + str(row))
    i += 1

choose = int(input("Type a row number: "))
del list_of_book[choose]
print(list_of_book)

replace = str(input("Type your replacing data: \n"))
list_of_book[choose] = (replace + "\n")
print(list_of_book)

file = open("Books.csv", "w")

for row in list_of_book:
    file.write(row)

file = open("Books.csv", "r")
print(file.read())

# Challenge 117

quiz_file = open("Quiz_Record.csv", "a")
quiz_list = ['Where are you from?', 'How old are you?', 'What is your name?', 'What is your occupation?', 'How is your father?', 'What is your graduate GPA?',
             'Do you prefer tea/coffee?']

quiz_one = quiz_list[random.randint(0, 6)]
quiz_file.write("\n" + quiz_one + "\n")
user_from = input(quiz_one)
quiz_file.write(user_from + "\n")

quiz_two = quiz_list[random.randint(0, 6)]
quiz_file.write(quiz_two + "\n")
user_age = input(quiz_two)
quiz_file.write(user_age + "\n")

quiz_file = open("Quiz_Record.csv", "r")
print(quiz_file.read())