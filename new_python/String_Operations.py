# Strings append shown below:

name = input("Please enter name: ")
print("My name is", name)

name = input("Please enter name: ")
print("My name is", name, "I got it.")

name = input("Please enter name: ")
print("My name is " + name + " I got it.")

age = input("Please enter your age: ")
print("My name is", name, "and my age is", age)

# The same expression with previous one.
print("My name is", name, "and my age is" + " " + age)

# Changing upper case to lower case

text = input("Please enter a string: ")
text = str.lower(text)
print(text)
