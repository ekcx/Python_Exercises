# Challenge 069
# Creating a tuple that is containing the names of five countries.
# Tuples are constant when the program is running.
# Creating Tuples
country_tuple = ("The United States", "Germany", "Belgium", "The Netherlands", "Spain")
print(country_tuple[0:5])
print(len(country_tuple))

my_string = input("Please enter the country: ")

# The For loop that is searching entered country in the tuple positions, then display it.

for i in range(0, 5):
    if my_string == country_tuple[i]:
        print(f"The index of the country is {i}")