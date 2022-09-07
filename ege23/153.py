def f(a,b):
    if a == b:
        return 1
    if a > b :
        return 0
    return f(a,b - 8) + f(a,b // 2)

print(f(48,102) * f(49,5))