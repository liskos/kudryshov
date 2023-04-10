def f(n):
    b = bin(n)[2:]
    if int(b,2) % 2 == 0:
        b = "10" + b
    else:
        b = "1" + b + "01"
    return int(b,2)

for i in range(1,9):
    print(f(i))

