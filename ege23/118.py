a = [34]
for i in range(6):
    b = []
    for x in a:
        b.append(x + 1)
        b.append(x + 2)
        b.append(x * 2)
    a = b.copy()
print(len((sorted(set(a)))))
print((sorted(set(a))))
