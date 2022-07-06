def f(d):
    n = 33
    s = 4
    while s < 1725 :
        s = s + d
        n = n + 8
    return n


for i in range(1, 999):
    if f(i) == 153:
        break
for y in range(999, 1, -1):
    if f(y) == 153:
        break
print(i,",",y)