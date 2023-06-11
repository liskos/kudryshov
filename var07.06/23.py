def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    return f(a-sum(map(int,str(a))),b) + f(a // 2,b) + f(a - 1,b)

print(f(40,25)* f(25,10))