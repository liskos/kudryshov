def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(4,39):
    s = f(27,i)
    if s[-1] == 3:
        print(i)