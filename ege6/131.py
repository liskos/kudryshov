def f(s):
    n = 4
    while s <= 96:
        s = s + 8
        n = n + 5
    return n


m = 0
k = 0
for i in range(1,999):
    if f(i) == 54:
        m = i
        break
for i in range(999,1, -1):
    if f(i) == 54:
        m = i
        break
m = str(m)
k = str(k)
if int(m) > int(k):
    print(m + k)
else :
    print(k +m)