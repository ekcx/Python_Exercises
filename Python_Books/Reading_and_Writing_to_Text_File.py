# Defining a list and changing their elements while the program is running may be Ok.
# But, the data that's updated later on the running program will be lost.
# So, it is not adequate to use the list everywhere. Then, we have to get the new way.

file = open("Countries.txt", "w")
file.write("Italy\n")
file.write("Germany\n")
file.write("Spain\n")
file.write("Turkey\n")
file.write("The USA\n")
file.write("The Netherlands\n")
file.write("England\n")
file.write("Portugal\n")
file.write("Syria\n")
file.write("Deneme0\n")

for i in range(0, 3):
    file.write(input("Type a text: "))
    file.write("\n")

file = open("Countries.txt", "r")
print(file.read())

file = open("Countries.txt", "a")
file.write("France\n")
file.close()
