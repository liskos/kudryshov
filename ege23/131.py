def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 1,b) + f(a * 2,b) + f(a * 2 + 1,b)

a = int('100', 2)
b = int('11101',2)
print(f(a,b))