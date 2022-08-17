# Challenge 115

file = open("Books.csv", "r")
i = 0
for row in file:
    print(str(i) + "-" + row)
    i = i + 1

