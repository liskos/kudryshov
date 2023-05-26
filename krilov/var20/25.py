def pros(n):
    k = 0
    for i in range(1,int(n ** 0.5) + 1):
        if n % i == 0 and n // i != i:
            k+=2
        elif n % i == 0:
            k += 1
    return k == 2


def f(n):
    k = 0
    for i in range(2,n):
        if n % i == 0  and pros(i):
            k += i

    return k



k = 0
for i in range(550001,999999):
    d = f(i)
    if d % 10 == 7:
        k+=1
        print(i,d)
    if k == 5:
        break

