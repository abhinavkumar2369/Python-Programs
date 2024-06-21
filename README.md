![Banner](https://github.com/abhinavkumar2369/Python-Programs/assets/170245635/cbf304ad-3810-4305-941c-fa4ed565eb05)

## Overview 📝
- It is the collection of all the Basic Python Programs.







## Functions
- Write a function that takes a list of numbers and returns the largest number.
```py
def largest_number_in_list(list):
    if len(list)<1:
        print("Empty List")
        return
    else:
        largest = list[0]
        for a in list:
            if a>largest:
                largest = a
        return largest

list_1 = [10,24,9,5,31,20]
list_2 = []

print(largest_number_in_list(list_1))
print(largest_number_in_list(list_2))
```

- Write a function that takes a string and returns a new string with all the vowels removed.
```py
def remove_vowel(string):
    new_string = ''
    vowel = ['a','e','i','o','u']
    for a in string:
        if a.lower() in vowel:
            continue
        else:
            new_string += a
    return new_string

a = 'Hello I am Duck'
print(remove_vowel(a))
```

- Write a function that takes two lists and returns a new list containing the elements that are in both lists (intersection).

```py
def list_common_element(l1,l2):
    new_list = []
    for a in l1:
        if a in l2:
            if new_list.count(a):
                pass
            else:
                new_list.append(a)
    return new_list

a = [1,2,3,4,5]
b = [2,5,7,1,5,3]

print(list_common_element(a,b))
```







## Lists

- Write a program that removes all duplicate items from a list.
```py
def unique_element_list(list):
    new_list = []
    for element in list:
        if new_list.count(element) == 0:
            new_list.append(element)
    return new_list

list_1 = [1,2,3,1,4,2,5,6,5,6]
print(unique_element_list(list_1))
# Output ---> [1,2,3,4,5,6]
```


- Write a program that sorts a list of numbers in descending order.
```py
def descending_order(list):
    list.reverse()
    return list

list = [10,3,4,16,1]
print(descending_order(list))
```


- Write a program that finds the second-largest number in a list.
```py
def second_largest_element(list):
    if len(list)<2:
        print("Less than 2 Elements")
    else:
        list.sort(reverse = True)
        print(list[1])

l = [1,2,7,3,4,5,8]
m = []

second_largest_element(l)
second_largest_element(m)
```












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










## String
- Write a program that counts the number of occurrences of a specific character in a string.

```py
def character_occurrence(string,element):
    count = 0
    for a in string:
        if a == element:
            count += 1
    return count

string = "Hello I am ShyDuck"
count = character_occurrence(string)

print(count)
```

- Write a program that reverses a string.

```py
def reverse_string(s):
    return s[::-1]

def reverse_string_2(s):
    new_string = ''
    for a in range(len(s)):
        new_string = s[a] + new_string
    return new_string

a = "0123456789"

print(reverse_string(a))
print(reverse_string_2(a))
```

- Write a program that checks if a string is a palindrome (reads the same backward as forward).

```py
# ------------ Function 1 -------------

def palindrome_string_1(string):
    flag = True
    for index in range(len(string)):
        if string[index] == string[-index-1]:
            pass
        else:
            flag = False
            print("Not palindrome")
            break
    if flag:
        print("Palindrome")


# ------------ Function 2 -------------
# Reversing a string using slicing

def palindrome_string_2(string):
    if string == string[::-1]:
        print("Palindrome String")
    else:
        print("Palindrome String")


# Using Function 1
palindrome_string_1("Abhinav")
palindrome_string_1('abccba')


# Using Function 2
palindrome_string_2("Abhinav")
palindrome_string_2('abccba')
```