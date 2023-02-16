def f(n):
    b = bin(i)[2:]
    if b.count("1") > b.count("0") :
        b = b + "0"
    else :
       b = "11" + b
    if b.count("1") > b.count("0") :
        b =  b + "0"
        return int(b,2)
    else :
        b = "11" + b
        return int(b,2)

for i in range(1,999):
    if f(i) > 500:
        print(i)