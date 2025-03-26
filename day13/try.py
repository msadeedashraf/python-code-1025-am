"""
x = 6
print(x)
"""

"""
try:
    x = 6
    print(x)
except:
    print("An Error")
"""
"""
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  """
"""
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
"""
try:
    f = open("abc.txt")
    print(f.read())
    try:
        f = open("abc.txt", "a")
        f.write("\nLorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("File not read check your path or file name")
