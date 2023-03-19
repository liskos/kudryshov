def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(4,22):
    s = f(22,i)
    if s[-1] == 4:
        print(i)