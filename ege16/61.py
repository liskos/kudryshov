def f(n):
    if n <= 15 :
        return n * n + 3 * n + 9
    if n > 15 and n % 3 == 0 :
        return f(n-1) + n - 2
    if n > 15 and n % 3 != 0:
        return f(n-2) + n + 2


k = 0
for i in range(1,1001):
    a = list(map(int,str(f(i))))
    s = sum([i % 2 for i in a])
    if s == 0:
        k += 1
print(k)

