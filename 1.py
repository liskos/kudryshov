def f(n):
    return (n + 1) * (n + 1)


def g(n):
    return n * n


def a(k):
    i = 1
    while f(i) < g(i) + k:
        i += 1
    return i


for i in range(99999, 1, -1):
    if a(k) == 14:
        print(i)
        break
