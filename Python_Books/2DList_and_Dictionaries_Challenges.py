# Challenge 096 #
# Creating 2D List #

simple_2D_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(simple_2D_list)

# Challenge 097 #
row = int(input("Type row number: "))
column = int(input("Type column number: "))
print(simple_2D_list[row][column])

# Challenge 098 #
display = int(input("Type a displayed row number: "))
print(simple_2D_list[display])
simple_2D_list[display].append(display)
print(simple_2D_list)