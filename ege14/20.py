def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(1,36):
    s = f(i,6)
    if s[0] == 4:
        print(i)
