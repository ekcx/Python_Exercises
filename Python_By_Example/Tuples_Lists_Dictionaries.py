# Once a tuple is defined you cannot change what is stored in it.
# Tuples are usually for menu items that would not need to be changed.
# The contents of a List can be changed while the program is running and lists are one of the most common ways
# - to store a collection of data under one variable name in Python.
# List include different data types at the same type. But it is not recommended to use due to unwanted results.
# Arrays are used to store ONLY numbers in Python. In the other programming languages array corresponds
# -the Lists in Python.
# Dictionaries - the content of a dictionary can also be changed while the program is running.
# index of dictionary is not changed if other rows of data are added or deleted
# -while program is running unlike LIST.

# Tuple Declaration - The content of Tuples cannot be altered while the program is running.
fruit_tuple = ("Apple", "Banana", "strawberry", "Orange")
print(fruit_tuple.index("Apple"))
print(fruit_tuple.index("Banana"))
print(fruit_tuple.index("strawberry"))
print(fruit_tuple[0])
print(fruit_tuple[1])
print(fruit_tuple[2])

# List Declaration - The square brackets define this group of data as a list and therefore;
# The contents can be altered while the program is running
names_list = ["John", "Tim", "Sam"]
print("\n")
print(names_list[0])
print(names_list[1])
print(names_list[2])
print("\n")

# Deleting from the list will shift the old one to the deleted one.
del names_list[0]  # Deleting John and the list left 2 items
del names_list[0]  # Deleting Tim and the list left 1 item.
print(names_list[0])
# Appending to the list:
names_list.append(input("Add a name:"))
print(names_list[1])
names_list.append(input("Add a name:"))
print(names_list[2])
# Sorting alphabetical order:
names_list.sort()
