def f(a):
    p = set(range(37, 60+1))
    q = set(range(40, 77+1))
    for x in range(0, 100):
        c = (x not in p) or (not((x in q) and (x not in a)) or (x not in p))
        if not c:
            return False
    return True


a = set(range(1, 99))
for i in range(1, 99):
    a.remove(i)
    if not f(a):
        a.add(i)
print(a)
