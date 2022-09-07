def f(a,b):
    if a == b:
        return 1
    if a > b :
        return 0
    return f(a ,b - 1) + f(a,b % 10)

print(f(11,110111)) 