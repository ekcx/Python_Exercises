# Challenge 020
# Taking the name and get the length of the name
get_name = input("Type your name: ")
name_length = len(get_name)
print("Your name's length is", name_length)

# Challenge 021
# Taking name and surname, join together and calculate the length of that string
your_name = input("Type your name: ")
your_surname = input("Type your surname: ")
name = your_name + " " + your_surname
length_name = len(your_name) + len(your_surname)
print(name, length_name)

# Challenge 022
# Taking name and surname lower case and translate to title.
your_name = input("Type your name in lower case: ")
your_surname = input("Type your surname in lower case: ")
your_name = your_name.title()
your_surname = your_surname.title()
print(your_name, your_surname)

# Challenge 023
# get the nursery rhyme in one line. Display lenght of it. Get the starting and ending index.
# And print part of the specified string.

nursery_ryhme = input("Type the first line of nursery ryhme: ")
print(len(nursery_ryhme))
number = int(input("Starting:"))
number2 = int(input("Ending: "))
print(nursery_ryhme[number:number2]) # included number - not included number2

# Challenge 024
# get the name and capitaliza every letters of it.

get_name = input("Type your name: ")
get_name = get_name.upper()
print(get_name)

# Challenge 025

get_name = input("First Name: ")

if len(get_name) < 5:
    get_surname = input("Enter your surname: ")
    name = get_name + get_surname
    print(get_name.upper() + get_surname.upper())
else:
    print(get_name.lower())

# Challenge 026

pig_word = input("Type a Pig Latin Name:")

if pig_word[0] == "a" or pig_word[0] == "e" or pig_word[0] == "i" or pig_word[0] == "o" or pig_word[0] == "u":
    pig_word = pig_word + "way"
    print(pig_word)
else:
    pig_word = pig_word + "ay"
    print(pig_word)
