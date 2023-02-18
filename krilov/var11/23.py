def f(a,b):
    if a < b :
        return 0
    if a == b :
        return 1
    return f(a-1,b) + f(a // 3,b)

print(f(33,9) * f(9,1))