def f(s):
    n = - 5
    while s > 10:
        s = s - 8
        n = n + 3
    return n

m = 0
k = 0
for i in range(-991,999):
    if f(i) == 67:
        m = i
        break
for i in range(999,-991, -1):
    if f(i) == 67:
        m = i
        break
m = str(m)
k = str(k)
if int(m) > int(k):
    print(m + k)
else :
    print(k +m)