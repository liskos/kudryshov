def f(a,b):
    if a == b :
        return 1
    if a < b :
        return 0
    if a%3==0:
        return f(a - 2, b)
    return f(a - 2,b) + f(a//3*3,b)

a = int('212', 3)
b = int('10',3)
print(f(a,b))