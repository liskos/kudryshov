def f(n):
    global a
    if n in a :
        return a[n]
    if n < - 10:
        a[n] = 1
        return 1
    if n > 10:
        a[n] = f(n-1) + 3 * f(n-3) + 2
        return a[n]
    a[n] = -f(n-1)
    return a[n]

a = dict()
print(f(20))