def f(a):
    for x in range(1,999):
        z = (39**2+80**2 >x**2) or(65**2+72**2<x**2) or (((x <= 80) or (x>=119)) or (x in a))
        if not z :
            return False
    return True

a = set(range(1,999))
for i in range(1, 999):
    a.remove(i)
    if not f(a):
        a.add(i)
print(a)

