def f(n):
    b = bin(n)[2:]
    if b.count("1") > b.count("0"):
        b = b + "1"
    else:
        b = b + "0"
    if b.count("1") > b.count("0"):
        b = b + "1"
    else:
        b = b + "0"
    return int(b,2)

for i in range(1,100):
    print(f(i))

