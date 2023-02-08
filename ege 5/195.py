a = set()
k = 0
for i in range (1,1000):
    n = bin(i)[2:]
    n = str(n) + str(n.count("1") % 2)
    n = str(n) + str(n.count("1") % 2)

    print(int(n,2))

