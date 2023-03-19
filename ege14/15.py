def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(2,37):
    s = f(63,i)
    if str(s)[-1] == "3" and str(s)[-2] == "2" :
        print(i)


