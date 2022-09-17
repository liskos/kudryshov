a = [1]
for _ in range(8):
    b = []
    for x in a:
        b.append(x + 1)
        b.append(x * 2)
        b.append(x * 3)
    a = b.copy()

print(a.count(34))
