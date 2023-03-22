def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]


h = int("34",8)
for i in range(2,36):
    s = f(h,i)
    if s[-1] == 0 and s[-2] == 2  :
        print(i)


