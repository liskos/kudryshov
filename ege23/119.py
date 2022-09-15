a = [1]
for i in range(8):
    b = []
    for x in a:
        b.append(x + 1)
        b.append(x + 5)
        b.append(x * 3)
    a = b.copy()
k = 0
for i in range (1000, 1025):
    if i in a :
        k += 1
print(k)

