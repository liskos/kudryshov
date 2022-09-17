def f(a,b):
    if a == b :
        return 1
    if a < b :
        return 0
    s = str(a)[::1] + '0'
    if a == str(a)[::1] + '0':
        return f(a - 2, b)
    return f(a - 2,b) + f(int(s,3),b)

a = int('212', 3)
b = int('10',3)
print(f(a,b))