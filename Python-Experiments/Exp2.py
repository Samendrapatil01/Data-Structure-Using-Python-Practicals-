# Experiment 2: Decision Making and Loops

# Positive or negative number
n = int(input("Enter a number: "))
if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")

# Grade calculation
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Needs improvement")

# Find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest:", max(a, b, c))

# Odd or even
n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")

# For loop
for i in range(1, 6):
    print(i)

# While loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Break and continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Sum of list elements
numbers = [10, 20, 30, 40]
print("Sum:", sum(numbers))

# Reverse a string
text = "Python"
print("Reversed:", text[::-1])
