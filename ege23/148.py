a = [2]
k = 0
for i in range(13):
    b = []
    for x in a:
        b.append(x + 3)
        b.append(x * 2 + 1)
    a = b.copy()
    k += 1
print(len(set(a)))
print(len(list(set(a))))

