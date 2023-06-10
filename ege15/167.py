def f(a):
    p = {2,4,6,8,10,12,14,16,18,20}
    q = {3,6,9,12,15,18,21,24,27,30}
    for x in range(1,1000):
        c = ((x not in p) or (x in a)) or ((x in a) or (x not in q))
        if not c:
            return False
    return True

b = []
for i in range(1,1000):
    if f(i):
        b.append(i)
print(len(b))
