def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(2,10):
    s = f(30,i)
    if len(s) == 4 and s[-1] == 0:
        print(i)