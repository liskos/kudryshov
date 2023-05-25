def f(n):
    s = ">" + 23 * "1" + n * "2" + 25 * "3"
    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s:
            s = s.replace(">1", "1>", 1)
        if ">2" in s:
            s = s.replace(">2", "3>", 1)
        if ">3" in s:
            s = s.replace(">3", ">11", 1)
    return s[:-1]

print(f(2))

def prost(n):
    a = []
    for i in range(1,n+1):
        if n % i == 0:
            a.append(i)
    if len(a) != 2:
        return False
    return True



for i in range(0, 100):
    s = f(i)
    if prost(sum(map(int, s))) == True:
        print(i)
print("||||",sum(map(int,"111111111111111111111113311111111111111111111111111111111111111111111111111")))