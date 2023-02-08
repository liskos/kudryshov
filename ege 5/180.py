i = 0
for i in range(1,128):
    i += 1
    n = bin(i)[2:]
    if len(n) < 8:
        n = "0" * (8-len(n)) + str(n)
    n = n.replace("0","2")
    n = n.replace("1","0")
    n = n.replace("2","1")
    n = int(n,2) + 1



    print(n,i)