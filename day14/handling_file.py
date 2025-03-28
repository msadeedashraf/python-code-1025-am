# f = open("../day13/mydemofile.txt", "a")
# f.write("This is my first file")

# Append a file
"""
f = open("./mydemofile.txt", "a")
dataString = "\nWelcome to CBC!"
f.write(dataString)
"""

"""
# Read File
f = open("./mydemofile.txt")
print(f.read())
"""

"""
# Reading a file from a location
#
f = open("D:\\CBC\\testPythonRead.txt", "r")
#print(f.read())
print(f.readline())
#print(f.readline())
"""

"""
f = open("mydemofile.txt", "r")
for x in f:
    print(x)
"""

"""
# Delete a file
import os

os.remove("D:\\CBC\\testPythonRead.txt")
"""

import os

if os.path.exists("../files/transactions.txt"):
    f = open("../files/transactions.txt", "r")
    myDataString = f.read()
    f.close()

    f2 = open("../files/transactions2.txt", "a")
    f2.write(myDataString)
    os.remove("../files/transactions.txt")
else:
    print("The file does not exist")

"""
import os
os.rmdir("myfolder")
"""
