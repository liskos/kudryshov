def f(n):
    s = "3" + "7" * n
    while "27" in s or "377" in s or "777" in s:
        if "27" in s :
            s = s.replace("27","32",1)
        if "377" in s :
            s = s.replace("377","27",1)
        if "777" in s :
            s = s.replace("777","3",1)
    return sum(map(int,s)) % 22 == 0

for i in range(10,100):
    if f(i):
        print(i)
