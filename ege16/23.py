def f(n):
    global g
    if n in g:
        return g[n]
    k = 1
    if n >= 1:
        k += 1
        k += f(n-1)
        k += f(n-3)
        k += 1
    g[n] = k
    return k

g = dict()
print(f(40))