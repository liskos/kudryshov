def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = "10" + b
        b = b[:-1] + "1"
    else:
        b = "1" + b
        b = b[:-2] + "10"
    return int(b,2)

for i in range(1,100):
    print(f(i),i)

