def f(n):
    if n > 25:
        return n * n + 4 * n + 3
    if n <= 25 and n % 3 == 0 :
        return f(n+1) + 2 * f(n+4)
    if n <= 25 and n % 3 !=0:
        return  f(n+2) + 3 * f(n + 5)


k = 0
for i in range(1,1001):
    if sum(map(int,str(f(i)))) == 24:
        k += 1
print(k)
