# Experiment 7: NumPy Arrays
# Install NumPy using: pip install numpy

import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])
print("Array:", a)
print("Type:", type(a))
print("Shape:", a.shape)
print("First element:", a[0])

# Common array creators
print("Zeros:", np.zeros(4))
print("Ones:", np.ones(4))
print("Range:", np.arange(1, 10, 2))
print("Linear values:", np.linspace(0, 1, 5))

# Two-dimensional arrays
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

print("Addition:\n", x + y)
print("Subtraction:\n", x - y)
print("Multiplication:\n", x * y)
print("Matrix multiplication:\n", x @ y)

# Array calculations
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Sorted:", np.sort([4, 1, 3, 2]))
print("Transpose:\n", x.T)
