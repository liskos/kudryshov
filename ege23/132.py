def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 1,b) + f(a * 2,b) + f(a * 2 + 1,b)

a = int('101', 2)
b = int('101110',2)
print(f(a,b))