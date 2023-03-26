def f(n):
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return n // i
    return 0

k=0
for i in range(650001,9999999):
    d = f(i)
    if d != 0 and f(d) != 0:
        k += 1
        print(i,d)
        if k == 6:
            break