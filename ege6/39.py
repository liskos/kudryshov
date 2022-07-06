def f(d):
    n = 0
    s = 24
    while s <= 1318:
        s = s + d
        n = n + 15
    return n


for i in range(1, 9999):
    if f(i) == 195:
        break
for y in range(9999, 1, -1):
    if f(y) == 195:
        break
print(i,",",y)