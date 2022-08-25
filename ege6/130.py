def f(s):
    n = 6
    while s <= 154:
        s = s + 12
        n = n + 3
    return n


m = 0
k = 0
for i in range(1,999):
    if f(i) == 42:
        m = i
        break
for i in range(999,1, -1):
    if f(i) == 42:
        m = i
        break
if m > k:
    print(str(m) + str(k))
else :
    print(str(k) + str(m))