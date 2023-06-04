def f(a):
    for x in range(0,1000):
        for y in range(0,1000):
            c = (not(x <= 9) or (x * x <= a)) and (not(y * y <= a) or (y <=9))
            if not c:
                return False
    return True

for i in range(1,1000):
    if f(i):
        print(i)