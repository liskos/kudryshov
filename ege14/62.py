def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(1,999):
    s = f(a,4)
    l = f(a,6)
    if l[-1] == 0 and s[-1] == 0:
        print(a)


