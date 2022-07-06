def f(d):
    n = 16
    s = 10
    while s <= 3120:
        s = s + d
        n = n + 8
    return n


for i in range(1, 9999):
    if f(i) == 264:
        break
for y in range(9999, 1, -1):
    if f(y) == 264:
        break
print(i,",",y)