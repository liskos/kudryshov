def f(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = b + b[-3:]
    else:
        b = b + bin((n % 5) * 5)[2:]
    return int(b,2)

print(f(4))
for i in range(1,1000):
    if f(i) > 256:
        print(i)
        break
