def f(n):
    k = 0
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            k += i
    return k




for i in range(550001,999999):
    d = f(i)
    if d % 10 == 7:
        print(i,d)
