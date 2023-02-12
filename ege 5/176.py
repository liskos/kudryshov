def f(n):
    b = bin(n)[2:]
    b = b.replace("0","2")
    b = b.replace("1","0")
    b = b.replace("2","1")
    b = int(b,2)
    return n + b

for i in range(1,999):
    if f(i) <= 123:
        print(i)