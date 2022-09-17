a = [3]
k = 0
for i in range(11):
    b = []
    for x in a:
        b.append(x + 1)
        b.append(x * 2 + 1)
    a = b.copy()
    k += 1
print(len(set(a)))
print(len(list(set(a))))

