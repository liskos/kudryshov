def f(n):
    b = bin(n)[2:]
    if int(b.count("1")) % 2 == 0:
        b = "10" + b
        b = b[:-1] + "1"
    if int(b.count("1")) % 2 == 1:
        b = "1" + b
        b = b[:-2] + "10"
    return int(b,2)

for i in range(1,999):
    if f(i) > 50 :
        print(i, f(i))