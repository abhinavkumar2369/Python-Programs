def factorial(n):
    if n<0:
        return "Error"
    fact = 1
    for a in range(1,n+1):
        fact = fact*a
    return fact


print(factorial(10))
# 120
