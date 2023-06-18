def f(p):
    s = "7" + p * "8"
    while "78" in s or "888" in s:
        if "78" in s:
            s = s.replace("78","8",1)
        if "888" in s :
            s = s.replace("888","7",1)
    return s

k = 0
for i in range(1000,2000+1):
    if sum(map(int,f(i))) == 16:
        k += 1
print(k)