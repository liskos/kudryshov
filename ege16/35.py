def f(n,m):
    if n<m:
        n,m = m,n
    if n != m :
        return f(n-m,m)
    else :
        return n

for i in range