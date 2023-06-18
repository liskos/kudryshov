def f(n):
    b = oct(n)[2:]
    if n % 7 == 0:
        b = b + b[-2:]
    else:
        b = b + oct(7 *(n % 7))[2:]
    return int(b,8)

a = set()
for i in range(1,3001):
    if f(i)<3000:
        a.add(f(i))
print(len(a))
