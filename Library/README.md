## Directory Structure 📁
<pre>
    Package
     |
     |---- __init__.py
     |---- english.py
           |
           |---- name()
     |---- math.py
           |
           |---- add(), subtract(), multiply(), divide()
</pre>


## ➡️ Importing Method 1
```py
from package.math import add,subtract,multiply,divide
from package.english import name

print(add(1,2))
# 3
print(multiply(2,3))
# 6
print(divide(3,4))
# 0.75
print(subtract(4,2))
# 2

name("Abhinav")
# My name is Abhinav
```



## ➡️ Importing Method 2

```py
from package import math, english

# ----------- Math Module ------------
print(math.add(1,2))
print(math.multiply(2,3))
print(math.divide(3,4))
print(math.subtract(4,2))

# --------- English Module -----------
english.name("Abhinav")

# -------------- Output --------------
# 3
# 6
# 0.75
# 2
# My name is Abhinav.
```
