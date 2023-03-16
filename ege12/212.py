def f(n):
    while "111" in n:
        n = n.replace("111","2", 1)
        n = n.replace("222", "1", 1)
    return n


for i in range(100,999):
    s = "1" * i
    if f(s) == "2":
        print(i)
        break
