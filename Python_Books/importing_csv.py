import csv

with open("Books.csv", "r") as read_object:
    csv_reader = csv.reader(read_object)
    list_of_csv = list(csv_reader)
    i = 0
    for row in list_of_csv:
        print(str(i) + "-" + str(row))
        i += 1

choose = int(input("Type a data row number delete & change: "))
i = 0

for i in list_of_csv:
    if choose == row:
        del list_of_csv[i]
        print(i)
    else:
        pass

print(list_of_csv)
