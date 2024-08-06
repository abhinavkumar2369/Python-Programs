# Global Variable
x = 10


def outer_func():
    x = 5
    def inner_func():
        nonlocal x
        x = 1
        print(x)
    inner_func()
    print(x)


outer_func()
# 1
# 1

print(x)
# 10