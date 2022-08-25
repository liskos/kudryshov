def f(s):
    n = 2
    while s < 85:
        s = s + 15
        n = n * 2
    return n


m = 0
k = 0
for i in range(1,999):
    if f(i) == 64:
        m = i
        break
for i in range(999,1, -1):
    if f(i) == 64:
        m = i
        break
if m > k:
    print(str(m) + str(k))
else :
    print(str(k) + str(m))