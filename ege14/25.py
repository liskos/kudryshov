def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(2,36):
    s = f(31,i)
    if s[-1] == 4:
        print(i)