def f(n, k):
    if n <= 5:
        return n, k +1
    if n > 5 and n % 5 == 0:
        g, k = f(n // 5 + 1, k)
        return n + g, k+1
    if n > 5 and n % 5 != 0:
        if k > 500:
            return 0, k
        g, k = f(n + 6, k)
        return n + g, k + 1

for i in range(1,1000):
    g, k = f(i, 0)
    if k <= 500 and g > 1000:
        print(i)
        break

