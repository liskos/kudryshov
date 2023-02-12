def f(n):
    a = sorted(list(str(n)))
    if a[0] != "0":
        amax = int(a[2] + a[1])
        amin = int(a[0] + a[1])
        return amax - amin
    elif a[1] != "0" :
        amax = int(a[2] + a[1])
        amin = int(a[1] + a[0] )
        return amax - amin
    else:
        return 0



for i in range(100,1000):
    if f(i) == 60:
        print(i)
        break