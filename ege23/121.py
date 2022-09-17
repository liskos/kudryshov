def f(a,b) :
    if a == b:
        return 1
    if a > b :
        return 0
    return f(a + 2,b) + f(a + 5,b)


for b in range(5, 999):
    if f(5,b) == 34:
        print(b)
        break
print(f(1, 27))
