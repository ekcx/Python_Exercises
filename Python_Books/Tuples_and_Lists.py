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

# Challenge 078

tv_programme = ["First", "Second", "Three", "Four"]
print(tv_programme[0])
print(tv_programme[1])
print(tv_programme[2])
print(tv_programme[3])

new_program = input("Type in a fifth program name: ")
tv_programme.append(new_program)
print(tv_programme)

# Challenge 079

nums = []

for i in range(0, 3):
    number = int(input("Type a number: "))
    nums.append(number)

print("Are you sure to add the last number to the list ? ")
yes_or_no = input("Type yes/no: ")
if yes_or_no == "no":
    nums.remove(2)
else:
    pass
print(nums)


