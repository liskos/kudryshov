a = [2]
k = 0
for i in range(15):
    b = []
    for x in a:
        b.append(x + 2)
        b.append(x * 2 + 1)
    a = b.copy()
print(len(set(a)))
print(len(list(set(a))))

