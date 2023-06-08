def f(a):
    for x in range(0,150):
        c = (x not in {1,2,3,4,5,6}) or not(x not in {3,6,9,12,15}) or(x in a)
        if not c:
            return False
    return True
c 
a = set(range(1,140))
for i in range(1,140):
    a.remove(i)
    if not f(a):
        a.add(i)

print(a)


