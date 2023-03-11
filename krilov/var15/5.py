def f(n):
    b = bin(n)[2:]
    b = b.replace("1","11")
    b = b.replace("0","00")
    return int(b,2)

for i in range(1,999):
    if f(i) > 32:
        print(f(i))
