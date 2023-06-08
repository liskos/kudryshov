def f(a):
    for x in range(1,1000):
        c = not((x % a != 0) and (x % 15 == 0)) or ((x % 18 != 0) or (x % 15 != 0))
        if not c:
            return False
    return True

for a in range(1,1000):
    if f(a):
        print(a)