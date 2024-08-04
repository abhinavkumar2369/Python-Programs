# Program to reverse a string


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