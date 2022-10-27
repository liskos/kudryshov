def f(n):
    global a
    a.append(n)
    if n > 0:
        d = (n%10 + f(n//10))
        a.append(d)
        return d
    else :
        return 0

for i in range(1,999):
    a=[]
    f(i)
    if a[1] > 51:
        print(i)
        print(f(i))
        break