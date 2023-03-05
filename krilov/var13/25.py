def f(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return n // i - i
    return 0

k = 0
for i in range(850000, 999999):
    s = f(i)
    if s != 0 and s % 13 == 0 :
        k += 1
        print(i,s)
    if k == 6:
        break