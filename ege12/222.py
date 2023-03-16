def f(n):
    while "111" in n :
        n = n.replace("111","2", 1)
        n = n.replace("222", "3", 1)
        n = n.replace("333", "1", 1)
    return n

 
k = 0
for i in range(1,101):
    s = "1" * i
    if f(s) == "321":
        k += 1
print(k)
