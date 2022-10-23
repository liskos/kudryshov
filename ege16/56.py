def f(n):
    if n > 20:
        return n * n * n + n
    if n <= 20 and n % 2 == 0 :
        return 3 * f(n+1) + f(n + 3)
    if n <= 20 and n % 2 != 0 :
        return f(n+2) + 2 * f(n+3)

k = 0
for i in range (1,1001):
    if str.f(i).find('1') == False:
        k +=1
print(k)