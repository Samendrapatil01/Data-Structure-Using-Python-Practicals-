# Experiment 6: Modules and Packages

import math
import random

# Using the math module
print("Square root:", math.sqrt(64))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))

# Using the random module
print("Random number:", random.randint(1, 10))

# User-defined module-style functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def add(a, b):
    return a + b

print("Is 7 prime?", is_prime(7))
print("Factorial of 5:", factorial(5))
print("Sum:", add(10, 20))

# A package contains related Python modules.
# Example structure:
# mypackage/
#     __init__.py
#     module1.py
#     module2.py
