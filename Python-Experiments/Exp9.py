# Experiment 9: Arrays and Sorting

import array

# Creating an array
numbers = array.array('i', [5, 2, 8, 1, 3])
print("Original array:", numbers.tolist())

# Adding and updating elements
numbers.append(10)
numbers.insert(1, 7)
numbers[0] = 4
print("Updated array:", numbers.tolist())

# Removing elements
numbers.remove(7)
numbers.pop()
print("After removal:", numbers.tolist())

# Searching and counting
print("Index of 8:", numbers.index(8))
print("Count of 2:", numbers.count(2))

# Bubble sort
def bubble_sort(values):
    values = values.copy()
    for i in range(len(values)):
        for j in range(len(values) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
    return values

data = [64, 34, 25, 12, 22, 11, 90]
print("Bubble sort:", bubble_sort(data))

# Insertion sort
def insertion_sort(values):
    values = values.copy()
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
    return values

print("Insertion sort:", insertion_sort(data))
