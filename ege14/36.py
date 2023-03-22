def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]


k = 0
for a in range(13,24):
    s = f(a,3)
    k += s.count(2)
print(k)


