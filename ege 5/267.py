def f(n):
    n2 = n
    n = bin(n)[2:]
    n1 = n[1:]
    n1 = n1.replace("1","2")
    n1 = n1.replace("0","1")
    n1 = n1.replace("2","0")
    n1 = "1" + n1
    n1 = int(n1,2)
    return n1 + n2




for i in range(1,999,2):
    if f(i) > 99:
        print(i)