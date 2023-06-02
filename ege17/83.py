def pr(n):
    p = 1
    while n > 0:
        p = p * (n % 10)
        n = n // 10
    return p

def s(n):
    p = 0
    while n > 0:
        p = p + n % 10
        n = n // 10
    return p

a = []
for i in range(1111,9999 + 1):
    if pr(i) != 0 and i % pr(i) == 0 and i % s(i) == 0:
        a.append(i)

print(len(a),max(a))

