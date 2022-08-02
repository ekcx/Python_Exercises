# Two-Dimensional List #
# It's like a two-dimensional array #

grades_one = [[45, 37, 54], [62, 58, 59],
              [49, 47, 60], [78, 83, 62]]

# Dictionary #

grades = [{"Ma": 45, "En": 37, "Fr": 54},
          {"Ma": 62, "En": 58, "Fr": 59},
          {"Ma": 78, "En": 47, "Fr": 60}]

print(grades_one[0][1])
print(grades[0]["En"])
print(grades_one[1][2])

print(grades[1]["Fr"])
print(grades[2]["En"])
print(grades[2]["Ma"])

# You can even go further and add a row index as follows.
grades = {"Susan": {"Ma": 45, "En": 37, "Fr": 54}, "Peter": {"Ma": 62, "En": 58, "Fr": 59}}
print(grades["Peter"]["En"])

# Example Code #
simple_array = [[2, 5, 8], [3, 7, 4], [1, 6, 9]]
print()

for i in range(0, 3):
    for j in range(0, 3):
        print(f"{simple_array[i][j]} ", end='')
    print()

print(simple_array)


# Creating 2D Dictionary using user-defined labels for the rows and columns.
data_set = {"A": {"x": 54, "y": 82, "z": 91}, "B": {"x": 75, "y": 29, "z": 80}}

print(data_set["A"])
print(data_set["B"])
print(data_set["A"])
print(data_set["B"]["y"])
print()

for i in data_set:
    print(data_set[i]["y"])
