def f(s):
    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s:
            s = s.replace(">1","222>",1)
        if ">2" in s:
            s = s.replace(">2","3>",1)
        if ">3" in s:
            s = s.replace(">3", "1>", 1)
    s = s[:-1]
    return sum(map(int,s))


def prov(n):
    a = set()
    for i in range(1,int(n ** 0.5 + 1)):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return len(a) == 2



for n in range(1,200):
    s = ">" + 11 * "1" + n * "2" + 11 * "3"
    print(n,f(s),prov(f(s)))