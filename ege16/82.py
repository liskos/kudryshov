def f(n):
    if n <= 5 :
        return n
    if n > 5 and n % 4 == 0:
        return n + f(n // 2 - 1)
    if n > 5 and n % 4 != 0:
        return n + f(n + 2)

for i in range(1,999):
    if f(i) > 1 :
        print(i)
