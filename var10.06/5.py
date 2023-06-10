def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + "010"
    else:
        b = b + bin(5 * (n % 3))[2:]
    return int(b,2)

a = []*2
for i in range(1,1000):
    if f(i) % 2 == 0 and f(i) > 300:
        a.append([f(i),i])
print(sorted(a))