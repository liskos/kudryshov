def f(s):
    n = 1
    while s < 185:
        s = s + 30
        n = n * 3
    return n

m = 0
k = 0
for i in range(1,999):
    if f(i) == 729:
        m = i
        break
for i in range(999,1, -1):
    if f(i) == 729:
        m = i
        break
m = str(m)
k = str(k)
if int(m) > int(k):
    print(m + k)
else :
    print(k +m)