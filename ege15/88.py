def f(a):
    for x in range(0,150):
        c = (x not in {2,4,6,8,10,12}) or (not((x in {3,6,9,12,15}) and (x not in a))or(x not in{2,4,6,8,10,12}))
        if not c:
            return False
    return True

a = set(range(1,140))
for i in range(1,140):
    a.remove(i)
    if not f(a):
        a.add(i)

print(a)


