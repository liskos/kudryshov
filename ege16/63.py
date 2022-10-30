def f(n):
    if n <= 13 :
        return n**3 + n * n + 1
    if n > 13 and n % 3 == 0:
        return f(n-1) + 2 * n * n - 3
    if n > 13 and n % 3 != 0:
        return f(n-2) + 3 * n + 6

k = 0
for i in range(1,1001):
    a = list(map(int,str(f(i))))
    s = sum([i % 2 for i in a])
    if s == 0:
        k += 1
print(k)

