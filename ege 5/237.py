def f(n):
    b = bin(i)[2:]
    if int(b,2) % 2 != 2:
        b = b + "0"
    else:
        b = "1" + b
    if b.count("1") % 2 == 0:
        b = b + "1"
        return int(b,2)
    else:
        b = b + "0"
        return int(b,2)

for i in range(1,999):
    if f(i) > 228:
        print(i)