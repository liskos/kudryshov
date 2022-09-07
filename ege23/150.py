def f(a,b):
    if a % 2 == 0 and a < 100:
        return 1
    if a > b or a == 10 or a == 15:
        return 0
    return f(a + 3,b) + f(a * 3,b)

print(f(3,100))