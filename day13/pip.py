# https://pypi.org/project/pip/

# cmd
# To list all packages
# >pip list

# >pip --version

# >pip install camelcase

# from camelcase import CamelCase
# c = CamelCase()
# or

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
