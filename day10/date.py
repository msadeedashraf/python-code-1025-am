"""
import datetime

x = datetime.datetime.now()
print(x)
"""

import datetime as dt

x = dt.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

x = dt.datetime(2020, 5, 17)

print(x)

# https://www.w3schools.com/python/python_datetime.asp
