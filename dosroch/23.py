def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    if a % 5 == 0:
        return f(a - 5, b) + f(a - 2, b) + f(a // 5,b)
    return f(a - 5, b) + f(a - 2, b)

print(f(49,13)*f(13,1))