def f(n):
    b = bin(n)[2:]
    o = b.count("1") % 2
    b = b + str(o)
    if b.count("1") > b.count("0"):
        b = b + "0"
    else :
        b = b + "1"
    return int(b,2)

for i in range(1,233):
    print(f(i))
