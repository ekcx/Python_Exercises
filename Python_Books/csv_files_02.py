import csv

# Challenge 111

# Create a .csv file that will store the following data. Call it "Books.csv"

book_file = open("Books.csv", "w")
book_file.write("To Kill A Mockingbird, Harper Lee, 1960\n")
book_file.write("A Brief History of Time, Stephen Hawking, 1988\n")
book_file.write("The Great Gatsby, F. Scott Fitzgerald, 1992\n")
book_file.write("The Man Who Mistook His Wife for a Hat, Oliver Scaks, 1985\n")
book_file.write("Pride and Prejudice, Jane Austen, 1813")

book_file = open("Books.csv", "r")
print(book_file.read())
book_file.close()

# Challenge 112

book_file = open("Books.csv", "a")
book_name = input("Type a book name, Author and Year: ")
book_file.write("\n" + book_name)

book_file = open("Books.csv", "r")
print(book_file.read())

# challenge 112
