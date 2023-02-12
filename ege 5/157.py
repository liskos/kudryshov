def f(n):
    b = bin(n)[2:]
    b = "0" * (8 - len(b)) + b
    b = b.replace("0", "2")
    b = b.replace("1", "0")
    b = b.replace("2", "1")
    n2 = int(b, 2)
    return n2 - n


for i in range(0, 256):
    if f(i) == 113:
        print(i)
