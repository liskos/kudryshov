def f(a, b):
    if a == b:
        return 1
    if a > b  :
        return 0
    return f(a, b - 1) + f(a, b - 3) + f(a, b % 3)

print(f(2, 22))

