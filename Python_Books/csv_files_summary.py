import csv

file = open("csv_files_summary.csv", "w")
new_record = "Kocatas, 73, Gemini\n"
file.write(new_record)
file.close()


for i in range(0, 4):
    file = open("csv_files_summary.csv", "a")
    new_record = input("Type your name, birth year and your sign of zodiac: ")
    file.write("\n")
    file.write(new_record)

file.close()
file = open("csv_files_summary.csv", "r")

for i in file:
    print(file.read())
    print("\n")

file.close()

# the sense of the csv write/read/append process; first define the operation, second do the operation, then close the
# connection.
