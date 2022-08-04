# Challenge 110

# Using Names.txt file, display the list of names.
# Ask the user to type in one of the names and then save all the names
# , except the one they entered into a new file called Names2.txt

printing_file = open("Names.txt", "r")
print(printing_file.read())
printing_file.close()

printing_file = open("Names.txt", "r")
user_name = input("Type a name that's in the list: ")
for user in printing_file:
    if user != user_name:
        printing_file = open("Names2.txt", "a")
        new_row = user
        printing_file.write(new_row)
        printing_file.close()
printing_file.close()

reading = open("Names2.txt", "r")
print(reading.read())

