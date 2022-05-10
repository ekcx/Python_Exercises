# Math Explanation

import math

number = math.pi  # This assing pi number with 15 decimal places.
print(number)
print(round(number, 2))  # It reduces to 2 decimal places.
print(math.sqrt(number))

print(2 ** 2)  # squared
print(2 ** 3)  # cube
print(2 ** 4)  # fourth

# Challenge 027
# Get the float number and multiply by 2
get_number = float(input("Please enter a float number: "))
print(get_number * 2)

# Challenge 028
# display only two decimal
print(round(get_number * 2, 2))

# Challenge 029
# get the number 500, sqrt() and round 2 places.
get_number = int(input("Please print a number over 500: "))
print(round(math.sqrt(get_number), 2))  # reducing 2 decimal places.

# Challenge 030
# Display pi number
print(round(math.pi, 5))

# Challenge 031
# get the radius and calculate the area of the circle
get_radius = float(input("Please enter the radius of circle: "))
print("The area of the circle is", math.pi * pow(get_radius, 2))

# Challenge 032
# get the radius and depth of a cylinder and calculate the total volume.

get_radius = float(input("Type a radius for a cylinder: "))
depth = float(input("Type a depth of cylinder: "))
total_volume = math.pi * pow(get_radius, 2) * depth
print(total_volume)

# Challenge 033