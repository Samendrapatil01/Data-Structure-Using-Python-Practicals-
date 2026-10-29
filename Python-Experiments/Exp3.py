# Experiment 3: Lists and Tuples

# Creating and accessing a list
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice:", numbers[1:4])

# Adding elements
numbers.append(60)
numbers.insert(1, 15)
numbers.extend([70, 80])
print("After adding:", numbers)

# Updating and removing elements
numbers[0] = 5
numbers.remove(30)
numbers.pop()
print("Updated list:", numbers)

# Sorting and reversing
numbers.sort()
print("Sorted:", numbers)
numbers.reverse()
print("Reversed:", numbers)

# Nested list
matrix = [[1, 2], [3, 4]]
print("Nested element:", matrix[1][0])

# Creating a tuple
items = (10, 20, 30, 40)
print("Tuple:", items)
print("First item:", items[0])

# Tuple operations
print("Length:", len(items))
print("Count:", items.count(20))
print("Index:", items.index(30))

# Convert tuple to list and back
temp = list(items)
temp.append(50)
items = tuple(temp)
print("Updated tuple:", items)
