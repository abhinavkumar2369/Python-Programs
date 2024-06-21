# Write a program that checks if a tuple contains a specific element.

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