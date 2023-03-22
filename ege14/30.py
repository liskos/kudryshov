def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(4,21):
    s = f(a,2)
    if s[-1] == 0 and  s[-2] == 1 and  s[-3] == 1 :
        print(a)


