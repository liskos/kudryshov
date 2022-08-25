def f(s):
    n = 600
    while n > s:
        s = s + 3
        n = n - 6
    return n

m = 0
k = 0
for i in range(-991,999):
    if f(i) == 210:
        m = i
        break
for i in range(999,-991, -1):
    if f(i) == 210:
        m = i
        break
m = str(m)
k = str(k)
if int(m) > int(k):
    print(m + k)
else :
    print(k +m)