def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 2 == 0:
        return f(n-1) + 2 * f(n//2)
    if n > 3 and n % 2 != 0:
        return f(n-1) + f(n-3)


k = 0
for i in range(1,999):
    if f(i) < 10 ** 8:
        k += 1
        print(k)