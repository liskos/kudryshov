def f(n):
    b = bin(n)[2:]
    b = "0" * (8 - len(b)) + b
    b = b[:-1]
    b = b[::-1]
    b = int(b,2)
    return b

for i in range(1,100):
    if f(i) == i:
        print(i)