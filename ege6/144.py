def f(x):
    a = 1
    b = a
    while a < x:
        c = a + b
        a = b
        b = c
    return b

for i in range(1,999):
    if f(i) == 55:
     print(i)