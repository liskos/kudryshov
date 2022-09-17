def f(a,b) :
    if a == b:
        return 1
    if a < b :
        return 0
    return f(a + 1,b) + f(a * 2,b) + f(a + a % 4,b)

k = 0
for a in range(1, 80 + 1 ):
    if f(a,80) <= 5:
        k += 1
print(k)
