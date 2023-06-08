def f(a):
    for x in range(1,10000+1):
        c = not((x % a != 0) and (x % 6 == 0)) or (x % 3 != 0)
        if not c:
            return False
    return True

for a in range(1,10000):
    if f(a):
        print(a)


