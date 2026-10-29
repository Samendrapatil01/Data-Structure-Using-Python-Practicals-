
# Experiment 01: Operators & Basic Syntax

# 1. Input and Output
print("Hello")
a, b = map(int, input("Enter a and b: ").split())
print("Sum =", a + b)

# 2. Variables and Dynamic Typing
x = 5
y = 3.14
z = "Hi"
print(x, y, z)

x = 10
print(type(x))
x = "Python"
print(type(x))

# 3. Multiple Assignment and Identity
a = b = c = 100
print(a, b, c)

x, y, z = 1, 2.5, "Python"
print(x, y, z)

a = 10
b = a
print(id(a), id(b))

# 4. Deleting Variables
del x

# 5. Arithmetic Operators
a, b = 15, 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# 6. Comparison Operators
a, b = 13, 33
print(a > b, a < b, a == b)
print(a != b, a >= b, a <= b)

# 7. Logical Operators
a, b = True, False
print(a and b)
print(a or b)
print(not a)

# 8. Bitwise Operators
a, b = 10, 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

# 9. Assignment Operators
a = 10
b = a
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

# 10. Identity Operators
a, b = 10, 20
c = a
print(a is not b)
print(a is c)

# 11. Membership Operators
x, y = 24, 20
my_list = [10, 20, 30, 40, 50]

print(x not in my_list)
print(y in my_list)

# 12. Ternary Operator
a, b = 10, 20
minimum = a if a < b else b
print("Minimum:", minimum)

# 13. Python Keywords
import keyword
print(keyword.kwlist)
