def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(1,26):
    s = f(i,2)
    if s[-3:] == [1,0,1]:
        print(i)