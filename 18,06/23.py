def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    return f(a-2,b) + f(a//3,b)

print(f(200,6) * f(6,2))