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

k = 0
for i in range(800,900):
    if f(i) == 30:
        k += 1
        print(i,k)
