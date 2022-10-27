def f(n):
    if n <= 5 :
        return n + 15
    if n > 5 and n % 2 == 0:
        return f(n // 2) + n**3 - 1
    if n > 5 and n % 2 != 0:
        return f(n-1) + 2 * n**2 + 1

k = 0
for i in range(1,1001):
    if str(f(i)).count('8') >= 2:
        k += 1
print(k)
