def f(n):
    if n <=  1:
        return n
    if n > 1 and n % 3 == 0:
        return n + f(n // 3 + 1)
    if n > 1 and n % 3 != 0:
        return 1000000000

for i in range(1,1000):
    print(i, f(i))
    if f(i) > 1000 and f(i) < 1000000:
        print(i)
        break