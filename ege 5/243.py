def f(n):
    b = bin(n)[2:]
    if b.count("1") == b.count("0"):
        b = b + b[-1]
    if b.count("1") < b.count("0"):
        b = b + "1"
    if b.count("1") > b.count("0"):
        b = b + "0"
    if b.count("1") == b.count("0"):
        b = b + b[-1]
    if b.count("1") < b.count("0"):
        b = b + "1"
    if b.count("1") > b.count("0"):
        b = b + "0"
    return int(b,2)

for i in range(91,900):
    if (f(i) % 2 == 0) and (f(i) % 4 != 0):
        print(i)