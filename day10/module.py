import testmodule as m

print(m.add(5, 6))
print(m.multiply(5, 6))
print(m.subtract(5, 6))
print(m.divide(5, 6))
print(m.pi)
print(m.person1["age"])

print(dir(m))


import platform

x = platform.system()
print(x)

print(dir(platform))


# Import From Module
# You can choose to import only parts from a module, by using the from keyword.

from testmodule import add

print(add(6, 9))

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
