def f(a):
    for x in range(1,100):
        f = ((x % 3 != 0) or  (x % 11 != 0 )) or (x + a >= 80)
        if not f:
            return False
    return True


for a in range(1,100):
    if f(a):
        print(a)
