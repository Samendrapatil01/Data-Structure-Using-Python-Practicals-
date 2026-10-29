# Experiment 5: Built-in and User-Defined Functions

import math

# Built-in functions
text = "python programming"
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Split:", text.split())
print("Replace:", text.replace("python", "AI"))

print("Square root:", math.sqrt(25))
print("Factorial:", math.factorial(5))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.8))

# Function with arguments and return value
def add(a, b):
    return a + b

print("Sum:", add(10, 20))

# Default arguments
def greet(name="Student"):
    print("Hello,", name)

greet()
greet("Samendra")

# Return multiple values
def calculate(a, b):
    return a + b, a - b

total, difference = calculate(20, 5)
print("Total:", total)
print("Difference:", difference)

# Variable-length arguments
def total(*numbers):
    return sum(numbers)

print("Total:", total(1, 2, 3, 4, 5))

# Lambda function
square = lambda n: n * n
print("Square:", square(6))
