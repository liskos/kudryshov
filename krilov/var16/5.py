def f(n):
    b = bin(n)[2:]
    b = b.replace("0","00")
    b = b.replace("1", "11")
    return int(b,2)

for i in range(1,444):
    if f(i) > 63:
        print(f(i),i)