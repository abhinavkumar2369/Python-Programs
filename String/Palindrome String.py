# Write a function to check whether a string is palindrome or not.

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