# I am proceeding to handle the rest of the book.
# The last challenge that I implemented: 069

# Example Code

fruit_tuple = ("Apple", "Banana", "Strawberry", "Orange")
print(fruit_tuple.index("Apple"))
print(fruit_tuple.index("Banana"))
print(fruit_tuple.index("Strawberry"))
print(fruit_tuple.index("Orange"))
print("\n")
print(fruit_tuple[0])
print(fruit_tuple[1])
print(fruit_tuple[2])
print(fruit_tuple[3])

names_list = ["John", "Tim", "Sam", input("Please enter a name: ")]
print(names_list[3])

names_list.append(input("Enter a name: "))
print(names_list[4])

# Delete name_list[1] index.
del names_list[1]

print(names_list[3])

# Sort the list by alphabetical order.
names_list.sort()

# Print the sorted list but do not change the original order.
print(sorted(names_list))

# Colours Dictionary

colours = { 1: "Red", 2: "Blue", 3: "Green" }
colours[2] = "Yellow"
print(colours[2])

# Creating List

x = [154, 634, 892, 345, 341, 43, 99, 192, 11, 0, 12, 34, 1]
print(len(x))

# This will display data in positions 1, 2, and 3.
print(x[1:4])























