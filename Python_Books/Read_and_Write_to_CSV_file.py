import csv

# Writing to the text file Stars2.csv a string line.

file = open("Stars2.csv", "w")
newString = "Brian, 73, Taurus\n"
file.write(newString)
file.close()

# Reading from the text file Stars2.csv

file = open("Stars2.csv", "r")
print(file.read())
file.close()

file = open("Stars2.csv", "a")
newString = "The last line of the Stars2.csv after appending itself.\n"
file.write(newString)
file.close()

file = open("Stars2.csv", "r")
print(file.read())
file.close()
