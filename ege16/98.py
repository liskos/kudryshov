def f(n):
    if n == 0 :
        return 0
    if n > 0 and n % 2 == 0 :
        return f(n//2) + 3
    if n > 0 and n % 2 != 0:
        return 2 * f(n-1) + 1

a =[]
for i in range(1,1001):
    a.append(f(i))
print(len(set(a)))