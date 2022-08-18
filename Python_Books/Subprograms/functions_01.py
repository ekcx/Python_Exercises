# warming up

def get_name():
    user_name = input("Type your name: ")
    return user_name


def printing_Msg(user):
    print("Halo!", user)


def main():
    user = get_name()
    printing_Msg(user)


main()


def get_data():
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    data_tuple = (user_name, user_age)
    return data_tuple


print(get_data())


def message(user_name, user_age):
    if user_age <= 10:
        print("Hi", user_name)
    else:
        print("Hello", user_name)

