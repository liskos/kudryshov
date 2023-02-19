def f(n):
    for i in range(2,int(n**0.5) + 1):
        if n  % i == 0:
            mind = i
            maxd = n // i
            return maxd - mind
    return 0

k = 0
for i in range (850001,999999):
    y = f(i)
    if y != 0 and y % 3 == 0 :
        k += 1
        print(i,y)
        if k == 6 :
            break


