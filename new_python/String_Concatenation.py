# Concatenating strings with the + operator!
# helper_string and string are different string variable.
# Everytime that we can enter any string in string, we are concatenating to helper_string.

helper_string = ""

while True:
    string = input("Enter: ")

    if string == "end":
        break
    else:
        helper_string += string + " "

print(helper_string)

var = ""
sentence = ""

while sentence != "end":
    sentence = input("Type any word: ")

    if sentence != "end":
        var += sentence + " "
    else:
        break

print(var)

# Mean, Summation, Count, Positive-Negative

number = 1
summation = 0
count = 0
positive_number = 0
negative_number = 0


while number != 0:
    number = int(input("Type a number: "))
    summation += number

    if number != 0:
        count += 1
        if number > 0:
            positive_number += 1
        else:
            negative_number += 1
    else:
        break

print("\n")
print(f"The summation is {summation}")
print(f"The mean is {summation / count}")
print(f"The positive number is {positive_number}")
print(f"The negative number is {negative_number}")
