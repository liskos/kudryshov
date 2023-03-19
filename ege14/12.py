def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(19,34):
    s = f(a,6)
    print(s.count(3))
    print(s)