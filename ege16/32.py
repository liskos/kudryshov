def f(n):
    if n < 10:
        return n
    else:
        m = f(n//10)
        d = m % 10;
        if m < d :
            return d
        else:
            return m

for i in range(999,1,-1):
    if f(i) > 7:
        print (i)
        print(f(i))
        