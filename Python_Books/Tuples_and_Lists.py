# Challenge 076 and 077

my_friends_list = []

for i in range(0, 3):
    my_friend = input("Type a friend name: ")
    my_friends_list.append(my_friend)

print(my_friends_list)

type_friend = input("Please enter a name that's in the list: ")

if type_friend in my_friends_list:
    print(my_friends_list.index(type_friend))
    question = input("Are you sure to invite this friend?")
    if question == "yes":
        print(my_friends_list)
    else:
        del my_friends_list[my_friends_list.index(type_friend)]

# del function needs the integer for its parameter.

print(my_friends_list)

yes_or_no = input("Do you want to add another friend? yes or no?")

if yes_or_no == "yes":
    my_friends_list.append(input("Type the another friend's name: "))
else:
    print(my_friends_list)

print(my_friends_list)

# Challenge 078 and 079 are the same with the previous examples. So, I do not need to implement again.

