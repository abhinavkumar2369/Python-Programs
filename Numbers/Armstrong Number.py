n = int(input("Enter a Number : "))

copy = n
sum = 0

while n:
    sum = sum + (n%10)**3
    n //= 10

if (copy == sum):
    print("------ Armstrong Number -------")
else:
    print("-------- Not Armstrong --------")