def f(n):
    if n <= 15:
        return n * n + 11
    if n > 15 and n % 2 == 0:
        return f(n // 2) + n**3 - 5 * n
    if n > 15 and n % 2 != 0:
        return f(n-1) + 2 * n + 3

k = 0
for i in range(1,1001):
    if str(f(i)).count('6') >= 3:
        k += 1
print(k)
