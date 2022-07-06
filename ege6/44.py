def f(d):
    n = 23
    s = 18
    while s <= 1977:
        s = s + d
        n = n + 6
    return n


for i in range(1, 9999):
    if f(i) == 53:
        break
for y in range(9999, 1, -1):
    if f(y) == 53:
        break
print(i,",",y)