def f(d):
    n = 1
    while d // n > 0 :
        d = d - 2
        n = n + 3
    return n


m = 0
k = 0
for i in range(1,999):
    if f(i) == 46:
        m = i
        break
for i in range(999,1,-1):
    if f(i) == 46:
        k = i
        break
print(m + k)
