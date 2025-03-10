# Patric Natindim
# March 9 2025

# Problem 5: Convert radians to degrees and compare it with the degrees function

import math

radians = float(input("Radians: "))

degrees = radians * (180 / math.pi)

degrees_function = math.degrees(radians)


print(f"Program Conversion: {degrees} degrees")
print(f"Math Module: {degrees_function} degrees")
