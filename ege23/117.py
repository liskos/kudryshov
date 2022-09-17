a = [1]
for i in range(7):
    b = []
    for x in a:
        b.append(x + 1)
        b.append(x + 5)
        b.append(x * 3)
    a = b.copy()
print(len(set(a)))
print(a)


