# Challenge 118

def ask_number():
    num = int(input("Type your integer: "))
    return num


def count_to_num(num):
    i = 1
    while i <= num:
        print(i)
        i = i + 1


def main():
    num = ask_number()
    count_to_num(num)


main()

