# ================================
# Python List and String Functions
# ================================

# 1. list() → Used to create list (like array) in Python
t = list(range(0, 10, 2))
print(t)  # [0, 2, 4, 6, 8]

# 2. len() → Returns number of elements in list
n = [10, 20, 30, 40]
print(len(n))  # 4

# 3. count() → Returns number of occurrences of specified item
n = [1, 2, 2, 2, 3, 3]
print(n.count(2))  # 3
print(n.count(8))  # 0

# 4. index() → Returns index of first occurrence
n = [1, 2, 2, 2, 3, 4]
print(n.index(2))  # 1
print(n.index(3))  # 4

# 5. append() → Adds item at last position
lst = []
lst.append("Deekshika")
lst.append("Sharma")
print(lst)  # ['Deekshika', 'Sharma']

lst = []
for i in range(0, 101, 10):
    lst.append(i)
print(lst)  # [0, 10, 20, ..., 100]

# 6. insert() → Insert item at given position
n = [1, 2, 3, 4, 5]
n.insert(1, 888)
print(n)  # [1, 888, 2, 3, 4, 5]

# Difference between append() and insert()
# append() → always adds element at the end
# insert() → adds element at specific index

# 7. extend() → Adds elements of another list
list1 = ["Paneer", "Pea", "Tomato"]
list2 = ["Good", "Vegetables"]
list1.extend(list2)
print(list1)  # ['Paneer', 'Pea', 'Tomato', 'Good', 'Vegetables']

# 8. remove() → Removes specific element
n = [10, 20, 30, 40]
n.remove(10)
print(n)  # [20, 30, 40]

# 9. pop() → Removes last element
n = [10, 20, 30, 40]
print(n.pop())  # 40
print(n)        # [10, 20, 30]

# 10. reverse() → Reverses the list
n = [10, 20, 30, 40]
n.reverse()
print(n)  # [40, 30, 20, 10]

# 11. sort() → Sorts the list
n = [20, 5, 15, 10, 0]
n.sort()
print(n)  # [0, 5, 10, 15, 20]

s = ["Apple", "Orange", "Grapes"]
s.sort()
print(s)  # ['Apple', 'Grapes', 'Orange']

# 12. copy() → Copies list
x = [10, 20, 30, 40]
y = x.copy()
y[1] = 777
print(x)  # [10, 20, 30, 40]
print(y)  # [10, 777, 30, 40]


# ================================
# String Operations
# ================================
s = "okay"
print(type(s))  # <class 'str'>

# Accessing using indexing
s = "okay"
print(s[3])   # y
print(s[-1])  # y

# Slicing
s = "abcdefghij"
print(s[2:7])   # cdefg
print(s[:7])   # abcdefg
print(s[2:])   # cdefghij
print(s[:1])   # a
