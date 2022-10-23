def f(n):
    if n <= 3:
        return  n
    if  n > 3 and n % 2 == 0:
        return 2 * n * n + f(n - 1)
    if n > 3 and n % 2 != 0:
        return n * n * n + n + f(n-1)

k = 0
for i in range(1,999):
    if f(i) < 10 ** 7:
        k +=1
        print(k)