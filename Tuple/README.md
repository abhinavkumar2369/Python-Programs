## Tuples
- Write a program that checks if a tuple contains a specific element.

```py
def tuple_element(tuple,element):
    if element in tuple:
        print("Element Present")
    else:
        print("Element Not Present")

# Tuple
t = (1,2,3,4,5,6)

# Element
e = 3
f = 10

# Function Call
tuple_element(t,e)
tuple_element(t,f)
```

- Write a program that iterates over a tuple and prints the index and value of each element.

```py
def index_value(t):
    for a in range(len(t)):
        print("Index ",a," --> ",t[a])

t = (1,2,3,4,5,7,8)
index_value(t)
```

- Write a program that concatenates two tuples.
```py
def tuple_concatenate(a,b):
    return a+b

a = (1,2,3,4,5)
b = (6,7,8,9,0)

c = tuple_concatenate(a,b)

print(c)
```
