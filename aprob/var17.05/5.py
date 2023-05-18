def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        s = b + b[-3:]
    else:
        s = b + bin((n%3)*3)[2:]
    return int(s,2)

for i in range(1,999):
    if f(i) < 76:
        print(i)
