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
