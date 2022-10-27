def f(n,m):
    if m == 0:
        d = 0
    else:
        d = n + f(n, m - 1)
    return d

a=[]
for i in range (1,99):
    for j in range(1,99):
        if f(i,j) == 30:
            a.append(i)
print(len(set(a)))