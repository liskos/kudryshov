def f(a,b):
    if a == b:
        return 1
    if a > b  or a == 33:
        return 0
    return f(a + 2,b) + f(a + 2,b)

print(f(2,14) * f(14,45))