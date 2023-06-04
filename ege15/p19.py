def f(a):
    for x in range(1,1000):
        c = (x % a == 0) or ((x % 21 != 0) and (x % 35 != 0))
        if not c:
            return False
    return True

for a in range(1,1000):
    if f(a):
        print(a)
