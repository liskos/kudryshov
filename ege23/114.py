a = [1]
for i in range(99):
    b = []
    for x in a:
        b.append(x + 1)
        b.append(x + 2)
        b.append(x * 2)
    a = b.copy()
    if a.count(28) > 0:
        print(i)
        break


