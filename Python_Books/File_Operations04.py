# Challenge 109

print(" 1) Create a new file \n 2) Display the file \n 3) Add a new item to the file")
choose_value = int(input(" Make a selection 1, 2 or 3: "))

if choose_value == 1:
    new_file = open("Subject.txt", "w")
    school_subject = input("Type a school subject: ")
    new_file.write(school_subject)
    new_file.close()
elif choose_value == 2:
    new_file = open("Subject.txt", "r")
    print(new_file.read())
    new_file.close()
elif choose_value == 3:
    new_file = open("Subject.txt", "a")
    school_subject = input("Type a new school subject: ")
    new_file.write("\n")
    new_file.write(school_subject)
    new_file = open("Subject.txt", "r")
    print(new_file.read())
    new_file.close()