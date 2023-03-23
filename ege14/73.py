def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(2,37):
    s = f(77,i)
    l = f(29,i)
    if s[-1] == 0 and l[-1] == 1:
        print(i)

