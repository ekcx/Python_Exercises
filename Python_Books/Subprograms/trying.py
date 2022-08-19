n = True
my_list = []
i = 0

while n:
    word = input("Please give a word: ")
    my_list.append(word)

    # At least, there are two string index to compare each other.
    if i >= 1:
        if my_list[i-1] == my_list[i]:
            n = False
        else:
            pass
    else:
        pass
    i = i + 1
