def f(a,b):
    if a > b :
        return 0
    if a == b :
        return 1
    return f(a +2,b) + f(a * 2,b) + f(a * 3,b)

print(f(1,6) * f(6,24))