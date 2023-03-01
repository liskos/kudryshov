def f(s):
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s :
            s = s.replace(">1","23>",1)
        if ">2" in s :
            s = s.replace(">2","2>",1)
        if ">0" in s :
            s = s.replace(">0","3>",1)
    return s

for n in range(0,20):
    s = ">" + 17 * "0" + n * "1" + 17 * "2"
    s = f(s)[:-1]
    s = sum(map(int,s))
    if s % 23 == 0:
        print(n)
        break


