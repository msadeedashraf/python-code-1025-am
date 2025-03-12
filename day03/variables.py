"""x = 5
y = "John"
print(x)
print(y)
"""

"""
x = str(3)  # x will be '3'
y = int(4)  # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)
print(x + str(y))
print(int(x) + y)
"""
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""
"""
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""
"""
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(fruits[0])
print(fruits[1])
print(fruits[2])

print(a)
print(b)
print(c)
"""
"""
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
"""
"""
x = "Welcome "
y = "to "
z = "CBC!"
print(x + y + z)
"""
"""
x = 5
y = "John"
# print(x + y)  # This will give error ---conversion type
print(x, y)
"""

# Global Variables
"""
x = "Sadeed"


def myfunc():
    x = "Arash"
    print("My Name is " + x)

    print(x)


def add(num1, num2):
    result = num1 + num2
    print(result)


print(x)


myfunc()

add(10, 20)
add(11, 20)
add(50, 20)
"""
# The global Keyword

"""
def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
"""

"""

x = "awesome"


def myfunc():
    global x
    x = "fantastic"
# print("Python is " + x)
myfunc()

print("Python is " + x)
"""
