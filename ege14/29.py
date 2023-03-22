def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(2,999):
    s = f(35,i)
    if s[-1] == 8 :
        print(i)


