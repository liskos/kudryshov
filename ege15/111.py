def f(a):
    p = {2,4,6,8,10,12,14,16,18,20}
    q = {5,10,15,20,25,30,35,40,45,50}
    for x in range(0, 100):
        c = ((x not in a) or (x not in p)) and ((x in q) or (x not in a))
        if not c:
            return False
    return True


a = set(range(1, 99))
for i in range(1, 99):
    a.remove(i)
    if not f(a):
        a.add(i)
print(a)
