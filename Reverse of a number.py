n = int(input("Enter a number : "))

reverse = 0
flag = False

if n<0:
    flag = True
    n = n*(-1)
    
while n:
    reverse = (reverse*10) + n%10
    n = n // 10

if flag:
    print(reverse*-1)
else:
    print(reverse)