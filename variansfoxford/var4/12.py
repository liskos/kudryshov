def f(n):
        s = ">" + 37 * "1" + n * "2" + 37 * "3"
        while (">1" in s) or (">2" in s) or (">3" in s):
            if ">1" in s:
                s = s.replace(">1","33>",1)
            if ">2" in s:
                s = s.replace(">2", "2>", 1)
            if ">3" in s:
                s = s.replace(">3", "1>", 1)
        return s

for i in range(0,100):
    s = f(i)[:-1]
    if sum(map(int, s)) % 17 == 0:
        print(i)
print(f(15).count("3"))
print(f(15).count("2"))
print(f(15).count("1"))
print("1231".split())