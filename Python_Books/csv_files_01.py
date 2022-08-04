# CSV stands for Comma Seperated Values and is a format usually associated with
# importing and exporting from spreadsheets and databases.

import csv

file = open("Stars.csv", "w")
new_record = "Brian, 73, Taurus \n"
file.write(str(new_record))
file.close()

file = open("Stars.csv", "a")
new_record = "John, 79, Gemini \n"
file.write(str(new_record))
file.close()

# For csv files:
# Once we open the csv file by using "w" attribute, to keep the data inside, we can use "a" attribute
# "a" -> append
# "w" -> write
# "r" -> read
# "x" -> creates new file and write to that file. If the file exist, then will crash.

file = open("Stars.csv", "a")
new_record = "Michael, 82, Unique \n"
file.write(str(new_record))
file.close()

file = open("Stars.csv", "a")
name = input("Enter name: ")
age = input("Enter age: ")
star = input("Enter a sign: ")
new_record = name + ", " + age + ", " + star + ""
file.write(str(new_record))
file.close()

file = open("Stars.csv", "r")
print(file.read())
file.close()

file = open("Stars.csv", "r")
reader = csv.reader(file)
rows = list(reader)

for i in range(0, 4):
    print(rows[i])

file = open("Stars.csv", "r")
search = input("Enter the data you are searching for: ")
reader = csv.reader(file)

for row in file:
    if search in str(row):
        print(row)

