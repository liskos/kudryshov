def f(n):
    n = n - (n % 4)
    b = bin(n)[2:]
    b = b + str(b.count("1") % 2)
    b = b + str(b.count("1") % 2)
    return int(b,2)

for i in range(1,999):
    if f(i) < 64:
        print(i,f(i))