def f(n):
    a = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.append(i)
            a.append(n//i)
    a = sorted(list(set(a)))
    return a


for i in range(110203, 110246):
    a = f(i)
    b = [j for j in a if j % 2 == 0 ]
    if len(b) == 4:
        print(*b)
