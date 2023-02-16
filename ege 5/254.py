def f(n):
    b = bin(n)[2:]
    if b.count("1") == b.count("0"):
        b = b + b[-1]
    elif b.count("1") < b.count("0"):
        b = b + "1"
    else:
        b = b + "0"
    if b.count("1") == b.count("0"):
        b = b + b[-1]
    elif b.count("1") < b.count("0"):
        b = b + "1"
    elif b.count("1") > b.count("0"):
        b = b + "0"
    if b.count("1") == b.count("0"):
        b = b + b[-1]
    elif b.count("1") < b.count("0"):
        b = b + "1"
    elif b.count("1") > b.count("0"):
        b = b + "0"
    return int(b,2)

for i in range(1,750):
    if (f(i) % 2 == 0) and (f(i) % 4 != 0):
        print(i)