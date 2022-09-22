def f(a):
    x = [a]
    for _ in range(5):
        y = []
        for g in x:
            y.append(g+1)
            y.append(g*2)
            y.append(g + g % 4)
        x = x + y
    return 80 in x

k = 0
for a in range(1, 80 + 1 ):
    if f(a):
        k += 1
print(k)
