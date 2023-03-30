def f(s):
    while ">0" in s or ">1" in s or ">2" in s:
        if ">0" in s:
            s = s.replace(">0","22>",1)
        if ">1" in s:
            s = s.replace(">1","2>",1)
        if ">2" in s:
            s = s.replace(">2", "1>", 1)
    s = s[:-1]
    return sum(map(int,s))


def prov(n):
    a = set()
    for i in range(1,int(n ** 0.5 + 1)):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return len(a) == 2



for n in range(1,20):
    s = ">" + 15 * "0" + n * "1" + 15 * "2"
    print(n,f(s),prov(f(s)))