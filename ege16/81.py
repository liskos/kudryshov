def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 5 == 0:
        return n + f(n // 5 + 1)
    if n > 5 and n % 5 != 0:
        return n + f(n + 2)

for i in range(1,1000):
    print(i, f(i))
    if f(i) > 1000:
        print(i)
        break
