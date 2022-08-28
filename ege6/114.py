def f(d):
    s = 5
    n = 7
    while s <= 3011:
        s = s + d
        n = n + 124
    return n

k = 0
for i in range(1,1000):
    if f(i) == 1247 and i % 10 == 8:
        k += 1
print(k)
