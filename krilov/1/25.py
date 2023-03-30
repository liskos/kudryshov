a = [11223]
for i in range(0,10):
    s = int("11" + str(i) + "223")
    a.append(s)
    s = int("110" + str(i) + "223")
    a.append(s)
    s = int("1100" + str(i) + "223")
    a.append(s)
for i in range(10,100):
    s = int("11" + str(i) + "223")
    a.append(s)
    s = int("110" + str(i) + "223")
    a.append(s)
for i in range(100,1000):
    s = int("11" + str(i) + "223")
    a.append(s)
k = 0
a = sorted(a)
for i in a:
    if i % 149 == 0:
        k += 1
        print(i,i // 149)
print(a)
print(k)


