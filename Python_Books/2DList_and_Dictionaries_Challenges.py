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
print(simple_2D_list[display_row])
simple_2D_list[display_row].append(display_row)
print(simple_2D_list)

# Challenge 099 #
display_column = int(input("Type a displayed column number: "))
#print(simple_2D_list[display_row][display_column])

yes_or_no = input(f"Will be deleted [{display_row}]x[{display_column}]? y/n ?")
if yes_or_no == "y":
    new_data = int(input("Type a new number: "))
    simple_2D_list[display_row][display_column] = new_data
else:
    pass

print()
print(simple_2D_list)

