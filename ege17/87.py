def f(n):
    k = 0
    for i in 7,13,17,19:
        if n % i == 0:
            k += 1
    return k == 2


a = []
s = 0
for i in range(25000,35000 + 1):
    if f(i):
        a.append(i)
        s += sum(map(int,str(i)))
print(len(a),s)


