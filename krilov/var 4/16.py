def f(n):
    global a
    if n in a :
        return a[n]
    if n < 3:
        a[n] = 1
        return 1
    if n > 2 and n % 2 == 1 :
        a[n] = f(n-1) - f(n-2)
        return f(n-1) - f(n-2)
    s = 0
    for i in range(1,n):
        s += f(i)
    a[n] = s
    return s

a = dict()
print(f(39))


