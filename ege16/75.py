def f(n):
    if n ==1001:
        return 1000000
    if n <= 1:
        return n
    if n > 1 and n % 2 == 0:
        return 1 + f(n//2)
    if n > 1 and n % 2 != 0 :
        return 1 + f(n+2)

for i in range(1,998):
    if f(i) < 10000:
        print(i, f(i))
print(2**15)