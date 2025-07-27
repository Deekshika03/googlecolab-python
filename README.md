# googlecolab-python
learning python

print("deekshika sharma")
print("uid: 24bai70756")
#additional operators 
x="2"
y=str(bool(4.8))
print(x+y)
d="2"
o=str(complex(4.8))
print(d+o)
x = 2       # integer
y = 3.3     # float
print("Addition result:", x + y)  # Output: 5.3
x = "2"     # string
y = "3"     # string
print(x + y)  # Output: 23
x = 2
y = bool(4.8)  # bool(4.8) returns True, which is 1 when added
print(x + y)   # Output: 3

x = "2"
y = bool(4.8)
print(x + y)  # TypeError: can only concatenate str (not "bool") to str
x = "2"     # string
y = 3       # float
print(x + y) # TypeError: can only concatenate str (not "float") to str

# subtraction_operations.py

# (1) Integer - Integer
a = 30
b = 10
print(a - b)  # 20

# (4) Float - Float
a = 30.0
b = 10.00
print(a - b)  # 20.0

# (5) Integer - Boolean
a = 20
b = bool(10)  # bool(10) returns True (1)
print(a - b)  #19

# multiplication_operations.py

# (1) Integer * Integer
a = 23
b = 35
print(a * b)  # Output: 805

# (2) Integer * Float
a = 23
b = 35.0
print(a * b)  # Output: 805.0

# (3) String * Integer
a = "23"
b = 5
print(a * b)  # Output: 2323232323

""" (4) String * String (TypeError)
try:
    a = "23"
    b = "5"
    print(a * b)
except TypeError as e:
    print("Error:", e)  # TypeError

# (5) String * Float (ValueError)
try:
    c = "1, 2, 3"
    print(float(c * 5))
except ValueError as e:
    print("Error:", e)  # ValueError """

# (6) String * Boolean
c = "123"
b = bool(1.3)  # True (1)
print(c * b)  # Output: 123

# (7) Boolean * Boolean
a = bool(4)  # True (1)
b = bool(4321)  # True (1)
print(a * b)  # Output: 1

# (8) List * Boolean
k = [1, 2, 3]
m = 99
print(bool(k) * m)  # True (1) * 99 = 99

""" (9) List * List (TypeError)
try:
    l = [1, 2, 3]
    k = [4, 5, 6]
    print(l * k)
except TypeError as e:
    print("Error:", e)  # TypeError : list & tupple"""

# (10) Boolean + Boolean (0 + 1)
x = bool()  # False (0)
y = bool(47)  # True (1)
print(x*y)  # Output: 0

# --- Division Operator (/): Performs division and returns float type ---

# Example (a)
a = 4.5
b = 2.0
print(a / b)  # Output: 2.25

# Example (b)
a = 4
b = 2
print(a / b)  # Output: 2.0 (float type)

# Example (c)
a = 5
b = 2
print(a / b)  # Output: 2.5

# Example (d)
a = 5
b = 2.0
print(a / b)  # Output: 2.5

# Example (e)
a = 2
b = complex(1, 0)
print(a / b)  # Output: (2+0j)

"""# Example (f)
x = (1, 2)   # tuple
y = (3, 5)
# print(x / y)  # TypeError: unsupported operand type(s) for / """

"""# Example (g)
a = bool(10)  # i.e., 1 (True)
b = bool(0)   # i.e., 0 (False)
# print(a / b)  # Output: ZeroDivisionError"""

# --- Modulo Division Operator (%): Returns the remainder ---

a = 3
b = 4
print(a // b)  # Output: 0 (integer division)
print(a % b)   # Output: 3 (remainder)

# Floor Division Operator

# Example 1
print(10 // 3)  # Gives 3

# Example 2
print(10.5 // 3)  # Gives 3.0

# Example 3
print(10 // 3.0)  # Gives 3.0

# Example 4
print(3.3333333333333335 // 1)  # Gives 3.0

# Based on your arguments:
# If both arguments are int type, then the result is int type.
print(10 // 2)  # 5
print(10 // 3)  # 3

# If at least one of the arguments is float type, then the result is also of float type.
print(10.0 // 3)  # 3.0
print(10 // 3.0)  # 3.0
print(10.0 // 3.0)  # 3.0

# Example with output as float for float inputs
print(20.5 // 2)  # 10.0
print(20 // 2.0)  # 10.0
print(20.5 // 2.0)  # 10.0
print(30 // 2)  # 15
print(30.0 // 2)  # 15.0

# Power Operator, or Exponential Operator
print(10 ** 2)  # Meaning is 10 to the power 2 is 100
print(3 ** 3)  # 27

# Relational Operators or Comparison Operators
a = 10
b = 20

print(a < b)  # True
print(a <= b) # True
print(a > b)  # False
print(a >= b) # False
print(a == b) # False
print(a != b) # True


# To know Unicode or ASCII value of characters, using ord() function
print(ord('a'))  # 97, Output shows ASCII value
print(ord('A'))  # 65, Output shows ASCII value

#compare string using characters using ASCII value
s1 = "Keemati"
s2 = "Shaanti"
# ASCII value of K is 107
# ASCII value of S is 115
print(s1 < s2)   # True
print(s1 <= s2)  # True
print(s1 > s2)   # False
print(s1 >= s2)  # False
print(s1 == s2)  # False
print(s1 != s2)  # True

# Relational Operators can be used with Boolean values (True & False)
# Here, True is 1 and False is 0
print(True > False)  # True (1 > 0)
print(True < False)  # False (1 < 0)
print(True >= False) # True (1 >= 0)
print(False <= True) # True (0 <= 1)
print(False == False) # True (0 == 0)
print(True == True) # True (1 == 1)

""" Example of Type-error
print(10 > 'Kismat') # Gives TypeError"""

# Conditional Statement (Implicit example based on the "if a > b" structure)
a = 10
b = 20

if a > b:
    print('a is greater than b')
else:
    print('b is greater')
# This will output: b is greater

# Equality Operators
# (==) Equal to
# (!=) Not Equal to

print(10 == 20)  # False
print(10 != 20)  # True

# Assignment Operators, used to assign value to variable
# like : a = 33

# Multiple assignment
a, b = 23, 24  # a = 23 and b = 24
print(f"a = {a}, b = {b}")

# Logical Operators: In Python, "and", "or", and "not" are the logical operators.

""" For BOOLEAN TYPES: 
and: if both arguments are True then only print True
or: if at least one argument is True then can print True
not: Complement"""

print(True and True)  # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

print(not True)   # False
print(not False)  # True

# Boolean examples
print(True or True)  # True
print(True or False) # True
print(not True)      # False
print(not False)     # True

# Script to visualize name and password set by user and print valid/invalid
name = "Kriti"
password = "Shiksha"

username_input = input("Enter name: ")
password_input = input("Enter password: ")

if username_input == name and password_input == password:
    print("Valid")
else:
    print("Invalid")
   
# Bitwise Operators
# Bitwise operators are applicable only for int and Boolean types.
# Various bitwise operators used in Python are:

# Bitwise and (&)
# Bitwise or (|)
# Bitwise XOR (^)
# Bitwise Complement (~)
# Bitwise Left Shift Operator (<<)
# Bitwise Right Shift Operator (>>)

# Example for bitwise AND
 print(5 & 3) # Binary of 5 is 101, Binary of 3 is 011. Result 001 (1)

# Example for bitwise OR
 print(5 | 3) # Binary of 5 is 101, Binary of 3 is 011. Result 111 (7)

# Example for bitwise XOR
 print(5 ^ 3) # Binary of 5 is 101, Binary of 3 is 011. Result 110 (6)

# Example for bitwise Complement
 print(~5) # -(5+1) = -6

# Example for bitwise Left Shift
 print(5 << 1) # 5 * (2^1) = 10

# Example for bitwise Right Shift
 print(5 >> 1) # 5 // (2^1) = 2
