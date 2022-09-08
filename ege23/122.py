def f(a,b) :
    if a == b:
        return 1
    if a > b :
        return 0
    return f(a + 2,b) + f(a + 4,b) + f(a + 5,b)


for b in range(32, 999):
    if f(31,b) == 1001:
        print(b)
        break
print(f(31, 40))
print(f(31,60))
print(f(31,50))
print(f(31,55))