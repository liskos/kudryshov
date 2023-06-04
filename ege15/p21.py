def f(n):
    for x in range(1,100):
        c = (x & n == 0) or ((x & 20 != 0) or (x & 5 != 0))
        if not c:
            return False
    return True

for i in range(1,100):
    if f(i):
        print(i)