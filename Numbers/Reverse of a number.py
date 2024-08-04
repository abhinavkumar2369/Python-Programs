# Reversing a Number

def reverse_number(n):
    flag = False
    rev = 0
    if n<0:
        n = -n
        flag = True
    while n:
        rev = (rev*10) + (n%10)
        n = n//10
    if flag:
        rev = -rev
    return rev


# Checking
print(reverse_number(6789))
print(reverse_number(-1234))