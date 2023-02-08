for i in range(1,1000):
    n = bin(i)[2:]
    if n.count("1") > n.count("0"):
        n = str(n) + "1"
    else :
        n = str(n) + "0"
    n = int(n,2)

    print(n)
