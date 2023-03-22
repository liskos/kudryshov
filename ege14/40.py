def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(1,21):
    s = f(a,5)
    if s[-1] == 3 :
        print(a)


