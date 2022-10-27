def f(n):
    if n > 0:
        d = n%10+f(n//10)[0]
        return d, d
    else :
        return 0, n

for i in range (1,100000):
    a, b = f(i)
    if b > 32:
        print(i, a)
        break
