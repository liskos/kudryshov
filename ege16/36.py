def f(n,m):
    if m == 0 :
        return n
    else :
        return f(m,n % m)


a = []
for i in range(100,1001):
    for j in range (100,1001):
        if f(i,j) == 30 :
            a.append(i)
print(len(set(a)))
