def factorial(num, show=False):
    import math
    res = math.factorial(num)
    if show:
        for i in range(num, 0, -1):
            print(i, end=" x " if i > 1 else " = ")
    return res

print(factorial(6, show=True))
print(factorial(8))