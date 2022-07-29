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

# This for loop display the numbers in x.
for i in x:
    print(i)

num = int(input("Enter number: "))

# if num is in x, it dipslays the index.
if num in x:
    print(num, "is in the list")
    print(x.index(num))
else:
    print("not in the list.")

# Inserting the number 420, to the 2. position.
x.insert(2, 420)
# This will change the index numbers of the items in the list.

# Removing the item from the list. This is useful if you do not know the index of that item.
# If the item is more than one in the list, the first one will be deleted.
x.remove(0)
print(x[9])
# will display as 11 instead of 0. because of deleting from the list by using x.remove() method.

# Appending to the end of list:
x.append(5)
print(x[13])

# Challenge 069

# Create a tuple which has 5 different countries.

country_tuple = ("The US", "The Great Britain", "Germany", "Poland", "The Netherlands")

print("\n")

for i in country_tuple:
    print(country_tuple[country_tuple.index(i)])

position = input("country name you prefer: ")
print("The index of your preferred country is: ")
print(country_tuple.index(position))


# Challenge 070
give_number = int(input("Please enter a number that's the country position: "))
print(country_tuple[give_number])

# Challenge 071

list_sports = ["Swimming", "Boxing"]
# list2_sports = ["Basketball", "Baseball", "Football", "Ice Hookey"]
sport = input("Type your fav. sport: ")
list_sports.append(sport)
list_sports.sort()
print(sorted(list_sports))












