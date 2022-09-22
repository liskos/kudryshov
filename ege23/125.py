def f(a,b):
    if a == b:
        return 1
    if a > b  or a == 33:
        return 0
    x = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    y = min([i for i in x if i > a])
    return f(a + 2,b) + f(y,b)

print(f(2,14) * f(14,45))