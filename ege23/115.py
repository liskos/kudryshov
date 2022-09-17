a = [1]
for i in range(99):
    b = []
    for x in a:
        b.append(x + 1)
        b.append(x + 5)
        b.append(x * 3)
    a = b.copy()
    if a.count(111) > 0:
        print(i)
        break


