# Challenge 086

password = input("Please type your password: ")
password2 = input("Please type your password: ")

if password == password2:
    print("Thank You.")
elif password.lower() == password2.lower():
    print("The password the same but in different case.")
else:
    print("Incorrect Password!")

# Challenge 087

my_string = "Hello!"

for i in range(-1, -1 * len(my_string) -1, -1):
    print(my_string[i])

