def f(n):
    if n < 3 :
        return n + 1
    if n >= 3 and n % 2 == 0:
        return 100000
    if n >= 3 and n % 2 != 0:
        return f(n-2) + n - 2

k = 0
for i in range (1,999):
    print(i,f(i))
    if 99 < f(i) < 1000 :
        k += 1
print(k)