def f(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]

a = []
for i in range(255,4095+1):
    if (f(i).count("1") == 1 or f(i).count("0") == 0) and i % 2 == 0 and i % 5 == 0 and i % 20 !=0 :
        a.append(i)

print(len(a),sum(a))

print(f(9))