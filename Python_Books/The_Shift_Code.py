# Challenge 146

message = input("Please type your message: ")
encoding = []
decoding = []
n = True


def encode_message(msg):
    for i in range(0, len(message)):
        number = ord(message[i]) + 1
        encoding.append(chr(number))

    return encoding


def decode_message(msg):
    for i in range(0, len(encoding)):
        number2 = ord(encoding[i]) - 1
        decoding.append(chr(number2))

    return decoding


while n:
    print("1) Make a code")
    print("2) Decode a message")
    print("3) Quit")

    selection = int(input("\nEnter your selection: "))
    if selection == 3:
        n = False
    elif selection == 2:
        print(decode_message(message))
    elif selection == 1:
        print(encode_message(message))
    else:
        pass
