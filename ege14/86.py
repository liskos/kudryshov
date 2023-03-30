def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(2,999):
    s = f(79,i)
    l = f(111,i)
    if s[-1] == 2 and l[-1] == 1:
        print(i)

