# Program to check whether the number is a perfect square or not

import math

def perfect_square(n):
    m = n**0.5
    m = math.floor(m)
    if (m**2 == n):
        return 1
    else:
        return -1


print(perfect_square(2))
# -1

print(perfect_square(4))
# 1