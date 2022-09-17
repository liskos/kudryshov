def f(a,b):
    if a == b :
        return 1
    if a < b :
        return 0
    x = len(bin(a)[2:]) - 1
    s = '1' + '0' * x
    if a == int(s,2):
        return f(a - 1, b)
    return f(a - 1,b) + f(int(s,2),b)

a = int('10001', 2)
b = int('1',2)
print(f(a,b))