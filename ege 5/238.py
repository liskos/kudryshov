def f(n):
    b = int(str(n) + str(n % 10))
    b = bin(b)[2:]
    if b.count("1") % 2 !=0 :
        b = b + "1"
    else :
        b = b + "0"
    return int(b,2)

for i in range(1,999):
    if f(i) > 413:
        print(i)