a = [3]
k = 0
for i in range(12):
    b = []
    for x in a:
        b.append(x + 1)
        b.append(x * 2 - 3)
    a = b.copy()
    k += 1
print(len(set(a)))
print(len(list(set(a))))

