def f(n):
    s = 2 * n
    if n > 1 :
        s += n-5
        s += f(n-1)
        s += f(n-2)
    return s

for i in range(1,999):
    if f(i) > 500000:
        print(i, f(i))
        break