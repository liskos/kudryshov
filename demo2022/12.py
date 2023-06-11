def f(n):
    s = ">" + 39 * "0" + n * "1" + 39 * "2"
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1","22>",1)
        if ">2" in s:
            s = s.replace(">2","2>",1)
        if ">0" in s:
            s = s.replace(">0","1>",1)
    s = s[:-1]
    return sum(map(int,s))

def g(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return len(a) == 2

for i in range(1,1000):
    if g(f(i)):
        print(i,f(i))
        break
