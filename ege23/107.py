a = [3]
for _ in range(7):
    b = []
    for x in a:
        b.append(x + 1)
        b.append(x + 4)
        b.append(x * 2)
    a = b.copy()

print(a.count(27))
