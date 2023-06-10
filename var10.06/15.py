def f(a):
    p = set(range(5,54+1))
    q = set(range(50,93+1))
    k = 0
    for x in range(1,1000):
        s = not((x not in p) and (x in q)) or (x > a)
        if not s:
            k+=1
            if k != 20:
                return False
    return True


for i in range(1,1000):
    if f(i):
        print(i)