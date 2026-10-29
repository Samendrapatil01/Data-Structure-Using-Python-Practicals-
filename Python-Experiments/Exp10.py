# Experiment 10: Linear and Binary Search

# Linear search
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

numbers = [10, 20, 30, 40, 50]
target = int(input("Enter number to search: "))

result = linear_search(numbers, target)
if result != -1:
    print("Found at index:", result)
else:
    print("Element not found")

# Binary search
def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

numbers.sort()
print("Sorted list:", numbers)

result = binary_search(numbers, target)
if result != -1:
    print("Found at index:", result)
else:
    print("Element not found")
