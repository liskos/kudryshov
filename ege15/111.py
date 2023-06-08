def f(a):
    p = {2,4,6,8,10,12,14,16,18,20}
    q = {3,6,9,12,15,18,21,24,27,30}
    for x in range(1, 1000):
        c = ((x not in a) or (x not in p)) and ((x in q) or (x not in a))
        if not c:
            return False
    return True


m = 0
for i in range(1, 150):
    for j in range(i, 150):
        a = set(range(i, j))
        if f(a) and (len(a) > m) :
            m = len(a)
print(m)
