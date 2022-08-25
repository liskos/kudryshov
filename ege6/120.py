def f(s):
    n = 1
    while s < 45:
        s = s + 8
        n = n * 3
    return n

k = 0
for i in range(1,999):
    if f(i) == 243:
        k += 1
print(k)