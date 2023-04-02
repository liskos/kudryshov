def f(a, i):
    s = []
    while a != 0:
        s.append(a % i)
        a = a // i
    return s[::-1]


for i in range(2,11):
    print(f(538,i),sum(f(538,i)),"|",i)