def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[-3:]
    if n % 3 != 0:
        b = b + bin(3 * (n % 3))[2:]
    return int(b,2)

a = []
for i in range(1,1000):
    if f(i) < 100:
        a.append(i)
print(a)
