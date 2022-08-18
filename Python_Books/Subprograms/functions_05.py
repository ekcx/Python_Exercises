# Challenge 121
def list_names():
    names_list = ["John", "Brian", "Travis", "David", "Sullivan"]

    print("1) Add a name to the list\n")
    print("2) Change the name from the list\n")
    print("3) Delete a list from the list\n")
    print("4) View all of the names in the list:\n")
    choose = int(input("Choose one:"))

    n = True

    while n:
        if choose == 1:
            adding_name = input("Type a new name: ")
            names_list.append(adding_name)
            print(names_list)
            n = False
        elif choose == 2:
            print(names_list)
            changing_name = int(input("Type a changing name index from the list: "))
            new_name = input("Type a new name: ")
            names_list[changing_name] = new_name
            print(names_list)
            n = False
        elif choose == 3:
            print(names_list)
            deleting_name = int(input("Type a name index that'll delete: "))
            del names_list[deleting_name]
            print(names_list)
            n = False
        elif choose == 4:
            for i in range(0, len(names_list)):
                print(names_list[i])
            n = False
        else:
            list_names()
            n = False


list_names()
