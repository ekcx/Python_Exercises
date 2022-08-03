# Challenge 096 #
# Creating 2D List #

simple_2D_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(simple_2D_list)

# Challenge 097 #
row = int(input("Type row number: "))
column = int(input("Type column number: "))
print(simple_2D_list[row][column])

# Challenge 098 #
display_row = int(input("Type a displayed row number: "))

# print(simple_2D_list[display_row])
simple_2D_list[display_row].append(display_row)

# print(simple_2D_list)

# Challenge 099 #
display_column = int(input("Type a displayed column number: "))
# print(simple_2D_list[display_row][display_column])

yes_or_no = input(f"Will be deleted [{display_row}]x[{display_column}]? y/n ?")
if yes_or_no == "y":
    new_data = int(input("Type a new number: "))
    simple_2D_list[display_row][display_column] = new_data
else:
    pass

print()
print(simple_2D_list[display_row])

# Challenge 100 #

sales_person = {"John" : {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
                "Tom"  : {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
                "Anne" : {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
                "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}

print(sales_person["John"])

# Challenge 101

user_name = input("Type user name: ")
region_name = input("Type region name: ")
print(sales_person[user_name][region_name])
print(sales_person[user_name])

