# Ascii Code -> ord() provides a character' ascii code.
# Ascii Code -> chr() provides turning into ascii code to character.

my_string = input("Enter a message!")
my_string2 = []
my_string3 = []

for i in range(0, len(my_string)):
    number = ord(my_string[i]) + 1
    my_string2.append(chr(number))

print(my_string2)


for i in range(0, len(my_string2)):
    number2 = ord(my_string2[i]) - 1
    my_string3.append(chr(number2))

print(my_string3)