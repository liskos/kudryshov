def f(a,b):
    if a == b:
        return 1
    if a > b  or a == 11 or a == 18:
        return 0
    return f(a + 1,b) + f(a + 5,b) + f(a * 3,b)

k = 0
for i in range(1,999):
    if f(i) < 227:
        k += 1

print(f(4,8) * f(8,23))
print(k)