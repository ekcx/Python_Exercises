word = "ABcdefGH - 1234567"
print(word)

integerOfWord = int(len(word))
print(integerOfWord)

word = str.upper(word) # Equal word.upper().
print(word)

word = str.lower(word) # Equal word.lower().
print(word)

word = "john doe"
word = word.title() # Every words will be starting capital letter.
print(word)

word = word.capitalize() # Only starting word will start capital letter and the others will be lowercase.
print(word)

firstName = input("First Name: ")
surName = input("Sur Name: ")
name = firstName + surName
print(name)
