def f(d):
    n = 24
    s = 12
    while s <= 3004:
        s = s + d
        n = n + 3
    return n


for i in range(1, 9999):
    if f(i) == 75:
        break
for y in range(9999, 1, -1):
    if f(y) == 75:
        break
print(i,",",y)