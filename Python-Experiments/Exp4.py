# Experiment 4: Sets and Dictionaries

# Creating and updating a set
numbers = {10, 20, 30, 40}
numbers.add(50)
numbers.update([60, 70])
numbers.discard(20)
print("Set:", numbers)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric difference:", a ^ b)

# Creating a dictionary
student = {
    "name": "Sam",
    "branch": "AI-DS",
    "marks": 85
}
print("Student:", student)
print("Name:", student["name"])

# Adding and updating values
student["city"] = "Pune"
student["marks"] = 90
print("Updated:", student)

# Removing an entry
student.pop("city")
print("After removal:", student)

# Display dictionary entries
for key, value in student.items():
    print(key, ":", value)

# Simple marks analysis
marks = {"Python": 85, "Maths": 90, "DBMS": 78}
print("Total:", sum(marks.values()))
print("Highest:", max(marks.values()))
