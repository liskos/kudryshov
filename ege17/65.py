a = []
def f(n):
    p = 1
    while n > 0:
        p = p * (n % 10)
        n = n // 10
    return p

for i in range(8800,55535 + 1):
    if f(i) > 35 and "7" in str(i):
        a.append(i)

print(max(a),len(a))

