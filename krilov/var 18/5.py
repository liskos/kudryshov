def f(n):
    b = bin(n)[2:]
    b = b.replace("0","02")
    b = b.replace("1", "10")
    b = b.replace("02","01")
    return int(b,2)

for i in range(1,444):
    if f(i) < 256:
        print(f(i),i)