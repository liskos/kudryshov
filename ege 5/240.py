def f(n):
    s = bin(n)[2:]
    s = "0" * (4 - len(s)) + s
    return s

def alg(n):
    s = ""
    while n > 0:
        s = f(n % 10) + s
        n = n // 10
    s1 = ""
    for i in s:
        if i == "0":
            s1 += "1"
        else:
            s1 += "0"
    return int(s1,2)



for i in range(1,999):
    if alg(i) == 151:
        print(i)