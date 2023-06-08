def f(a):
    p = set(range(3, 33+1))
    q = set(range(22, 44+1))
    for x in range(0, 100):
        c = (x not in q) or ((x not in p) or (x in a))
        if not c:
            return False
    return True


a = set(range(1, 99))
for i in range(1, 99):
    a.remove(i)
    if not f(a):
        a.add(i)
print(a)
