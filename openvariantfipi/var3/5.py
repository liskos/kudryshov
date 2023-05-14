def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[-3:]
    else:
        s = (n % 3) * 3
        s = bin(s)[2:]
        b = b + s
    return int(b,2)

for i in range(1,100):
    print(f(i),i)

