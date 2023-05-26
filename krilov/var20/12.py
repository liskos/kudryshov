def f(n):
    s = ">" + 23 * "1" + n * "2" + 25 * "3"
    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s:
            s = s.replace(">1", "1>", 1)
        if ">2" in s:
            s = s.replace(">2", ">3", 1)
        if ">3" in s:
            s = s.replace(">3", ">11", 1)
    return s[:-1]

def prost(n):
    a = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            a.extend([i, n//i])
    return len(set(a)) == 2


for i in range(0, 100):
    s = f(i)
    if prost(sum(map(int, s))):
        print(i)
