j = 0
a = set()
for i in range (1,999):
    b = bin(i)[2:]
    if b.count("1") > b.count("0"):
        b = b + "0"
    else:
        b = b + "1"
    k = len(b)
    b = b[:k//2 - 1] + b[1 - k//2:]
    b = int(b,2)
    if 50 <= b <= 100:
        a.add(b)
print(len(a))



