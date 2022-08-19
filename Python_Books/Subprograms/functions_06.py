# Challenge 122

def file_operations():
    print("1) Add to file.\n")
    print("2) View all records.\n")
    print("3) Quit to program.\n")
    choose = int(input("Enter the number of your selection: \n"))
    salary_list = []
    n = True

    while n:
        if choose == 1:
            file = open("Salaries.csv", "w")
            salary_list.append(str(input("Type the name: ")))
            salary_list.append(str(input("Type the salary: ")))
            file.write(salary_list[0] + "," + salary_list[1] + "\n")
            n = False
            file.close()
        elif choose == 2:
            file = open("Salaries.csv", "r")
            print(file.read())
            n = False
            file.close()
        elif choose == 3:
            n = False
        else:
            print("There is an error!")


file_operations()
