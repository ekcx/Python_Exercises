t1 = ()     # Creating an empty tuple
t2 = (1, 3, 5)  # Creating a tuple with three elements
t3 = tuple([2 * x for x in range(1, 5)]) # Creating tuple 2, 4, 6, 8, 10 and like this.
print(t3)

t4 = tuple("abcd")  # Creating a tuple from a string
print(t4)

tuple1 = ("green", "red", "blue")  # Creating tuple
print(tuple1)

tuple2 = tuple([7, 1, 2, 23, 4, 5])     # Creating a tuple from a list
print(tuple2)

print("Length is", len(tuple2))
print("Max is", max(tuple2))
print("Min is", min(tuple2))
print("Sum is", sum(tuple2))

print("The first element is", tuple2[0])

tuple3 = tuple1 + tuple2
print(tuple3)

tuple3 = 2 * tuple1
print(tuple3)

print(tuple2[2 : 4])    # Slicing operator
print(tuple1[-1])

print(2 in tuple2)
print(25 in tuple2)

for v in tuple1:
    print(v, end = ' ')
print()