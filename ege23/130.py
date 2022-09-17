a = [10]

for i in range(5):
    b = []
    for x in a:
        b.append(x + 2)
        b.append(x + 3)
        b.append(x * 2)
    a = b.copy()
print(len(set(a)))
