def f(a,b) :
    if a == b:
        return 1
    if a > b :
        return 0
    return f(a + 1,b) + f(a + 5,b) + f(a * 3,b)


for b in range(1, 999):
    if f(1,b) == 175:
        print(b)
        break
print(f(1, b))
