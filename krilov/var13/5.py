def f(n):
    n = n - (n % 8) + (n % 2)
    b = bin(n)[2:]
    b = b + str(b.count("1") % 2)
    b = b + str(b.count("1") % 2)
    return int(b,2)

for i in range(1,999):
    if f(i) > 90:
        print(f(i),i)


