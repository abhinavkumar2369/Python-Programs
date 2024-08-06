def factorial_recursion(n):
    if n==1:
        return 1
    return n*factorial_recursion(n-1)


print(factorial_recursion(5))