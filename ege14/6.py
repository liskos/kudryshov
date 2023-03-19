def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(5,39):
    s = f(40,i)
    if s[-1] == 4:
        print(i)