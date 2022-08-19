# Challenge 123

# In Python, it is not technically possible to directly delete a record from a .csv file.
# Instead, you need to save the file to a temporary list in Python, make the changes to the list and,
# then overwrite the original file with the temporary list.

def file_operations():
    print("1) Add to file.\n")
    print("2) View all records.\n")
    print("3) Delete a record.\n")
    print("4) Quit to program.\n")

    choose = int(input("Enter the number of your selection: \n"))
    salary_list = []
    n = True

    while n:
        if choose == 1:
            file = open("Salaries.csv", "w")
            salary_list.append(str(input("Type the name: ")))
            salary_list.append(str(input("Type the salary: ")))
            file.write(salary_list[0] + "," + salary_list[1] + "\n")
            file.close()
            n = False

        elif choose == 2:
            file = open("Salaries.csv", "r")
            print(file.read())
            file.close()
            n = False

        elif choose == 3:
            file = open("Salaries.csv", "w")
            word = input("Type a name and salary: \n")
            file.write(str(word))
            file.close()
            n = False

        elif choose == 4:
            n = False
        else:
            file_operations()
            n = False


file_operations()