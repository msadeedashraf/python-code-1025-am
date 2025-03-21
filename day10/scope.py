# Local Scope


def add(num1, num2):
    result = num1 + num2
    return result


print(add(5, 6))


# Function Inside Function


def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

# Global Scope
x = 300


def myfunc():
    print(x)


myfunc()

print(x)

# Global Keyword


def myfunc():
    global x
    x = 300


myfunc()

print(x)

x = 300


####
def myfunc():
    global x
    x = 200


myfunc()

print(x)


# Nonlocal Keyword


def myfunc1():
    x = "Jane"

    def myfunc2():
        nonlocal x
        x = "hello"

    myfunc2()
    return x


print(myfunc1())


# https://www.w3schools.com/python/python_scope.asp
