def f(n):
    print(n)
    if n > 0:
        d = (n%10 + f(n//10))
        return d
    else :
        return 0

for i in range(1,999):
    if f(i) > 51:
        print(i)
        print(f(i))