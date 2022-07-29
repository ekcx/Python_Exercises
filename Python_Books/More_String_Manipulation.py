# More String Manipulation #

msg = "My First Message"
msg_second = "MY SECOND MESSAGE"
msg_third = "my third message"

if msg.isupper():
    print("UpperCase")
else:
    print("It is not upperCase")

if msg_second.isupper():
    print("UpperCase")
else:
    print("It is not upperCase")

if msg_third.islower():
    print("LowerCase")
else:
    print("It is not LowerCase")

message = "Hello Word!"

for letter in message:
    print(letter, end="*")

# Challenge 080
print()
name = input("Type your name: ")
print(name)
print("%d" % len(name))

surname = input("Type your surname: ")
print(surname)
print("%d" % len(surname))

new_string = name + " " + surname
print(new_string)
print(len(new_string))

# Challenge 081

course = input("Type a course that you like: ")
for i in course:
    print(i, end="-")

my_str = "Much Ado About Nothing"
print("Much Ado About Nothing")
starting = int(input("Please type starting point: "))
ending = int(input("Please type ending point: "))

for i in range(starting, ending+1):
    print(my_str[i])


upper_case = input("Type in a upper case string: ")

while not upper_case.isupper():
    print("The string is not in the uppercase form! You will write again the string untill to become uppercase idiot!")
    upper_case = input("Type in a upper case string: ")
