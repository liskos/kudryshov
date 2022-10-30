def f(n):
    if n < 3 :
        return n + 1
    if n >= 3 and n % 2 == 0 :
        return f(n-2) + n - 2
    if n >= 3 and n % 2 != 0:
        return 1000000000000000

k = 0
for i in range (1,999):
    print(i,f(i))
    if 10000 <= f(i) < 100000 :
        k += 1
print(k)