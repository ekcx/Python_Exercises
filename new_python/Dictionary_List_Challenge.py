# Challenge 072
# Creating a list and ask to choose a course that's the user dislike.
# Delete the dislike one from the course list.

course_list = ["Math", "Physics", "Geography", "Chemistry", "Calculus", "Marketing"]
print(course_list)

chosen_course = input("Please type a course name that's you dislike: ")

if chosen_course in course_list:
    position = course_list.index(chosen_course)
    print("You choose the index:", position, "And will be deleted.")
else:
    print("The chosen course is not in the list.")


del course_list[position]
print(course_list)

# Challenge 073

my_dictionary = {}

for i in range(1, 5):
    choose = input("Type 4 fav. foods: ")
    my_dictionary[i] = choose

print(my_dictionary)
dislike = int(input("Type a food to get rid of these food: "))
del my_dictionary[dislike]
print(my_dictionary)

# Challenge 074
my_colour_list = ["black", "red", "purple", "green", "blue", "white", "rose", "pink", "brown", "navy blue"]
print(my_colour_list)
start = int(input("Type a number between 0-4"))
end = int(input("Type a number between 5-9"))
print(my_colour_list[start:end])

# Challenge 075
my_number_list = [124, 221, 943]

for i in range(0, 3):
    print(my_number_list[i])

integer = int(input("Type a 3-digit integer: "))
if integer in my_number_list:
    print(my_number_list.index(integer))
else:
    print("There is no matches!")

