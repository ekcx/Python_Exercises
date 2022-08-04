# Challenge 108
# To write any lines the end of the file, we have to use "a" property of open() method
# so that, we may not lost the previous data on the file.

file_names = open("Names.txt", "a")
new_names = input("Type a new name to write the Names file: ")
file_names.write("\n")
file_names.write(new_names)
file_names.write("\n")
file_names.close()

read_names = open("Names.txt", "r")
print(read_names.read())
