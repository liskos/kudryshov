def f(n):
    print(n)
    if n > 10:
        d = n%10+f(n//10)
        return d
    else :
        return 0

for i in range (20,999):
    if f(i) > 32:
        print( 'x=', f(i))
        break
