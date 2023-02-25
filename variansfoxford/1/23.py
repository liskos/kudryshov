def f(a,b):
    if a > b and a == 23:
        return 0
    if a == b:
        return 1
    return f(a+1,b) + f(a * 2,b)

print(f(1,10))
print(f(1,16) * f(16,48))
