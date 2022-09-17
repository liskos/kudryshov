def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 2,b) + f(a + 3,b) + f(a * 4,b)

a = int('1', 4)
b = int('100',4)
print(f(a,b))