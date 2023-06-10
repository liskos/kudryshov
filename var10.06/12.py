def f(n):
    s = 40 * "1" + 40 * "2" + n * "3"
    while "23" in s or "12" in s or "32" in s:
        if "12" in s:
            s = s.replace("12","21",1)
        if "32" in s:
            s = s.replace("32", "1", 1)
        if "23" in s:
            s = s.replace("23", "2", 1)
    return s


print(f(2),sum(map(int,f(2))))
print(f(3),sum(map(int,f(3))))
print(f(4),sum(map(int,f(3))))
print(f(1500),sum(map(int,f(1500))))
for i in range(1,100):
    if sum(map(int,f(i))) == 100:
        print(i)


