# Write a program that iterates over a tuple and prints the index and value of each element.

def index_value(t):
    for a in range(len(t)):
        print("Index ",a," --> ",t[a])

t = (1,2,3,4,5,7,8)
index_value(t)