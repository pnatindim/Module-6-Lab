# Patric Natindim
# March 9 2025

# Problem 6: Calculate the factorial of a user input value and compare it with the factorial function

import math

value = int(input("Enter a number: "))

factorial = 1
for i in range(1, value + 1):
    factorial *= i

factorial_function = math.factorial(value)

# Print both results
print(f"Factorial Calculation: {factorial}")
print(f"Math Module: {factorial_function}")
