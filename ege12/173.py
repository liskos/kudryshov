def f(n):
    k = 8
    while k > 0 :
        n = n.replace("0","3",1)
        n = n.replace("1", "7",1)
        n = n.replace("2", "2",1)
        n = n.replace("3", "1",1)
        n = n.replace("4", "6",1)
        n = n.replace("5", "0",1)
        n = n.replace("6", "4",1)
        n = n.replace("7", "5",1)
        k = k - 1

    return n

b = "32006"
for i in range(1,14):
    b = f(b)
    print(b)


