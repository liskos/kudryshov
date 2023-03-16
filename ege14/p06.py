def f(n,i):
    a = []
    while n != 0:
        a.append(n % i)
        n = n // i
    return a[::-1]

for i in range(1,31):
    a = f(i,5)
    if a[0] == 3:
        print(i)
