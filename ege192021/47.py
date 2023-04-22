def f(n):
    b = []
    if n + 1 <= 60:
        b.append(n+1)
    if n * 2 <= 60:
        b.append(n * 2)
    if n * 3 <= 60:
        b.append(n * 3)
    return b


a = ["-1"] * 200
for i in range(200):
    if 36 <= i <= 60:
        a[i] = "0"
for i in range(61):
    if a[i] == "-1" and  any(a[j] == '0' for j in f(i)):
        a[i] = "1"
for i in range(61):
    if a[i] == "-1" and  all(a[j] in '1' for j in f(i)):
        a[i] = "2"
for i in range(61):
    if a[i] == "-1" and  any(a[j] == '2' for j in f(i)):
        a[i] = "3"
for i in range(61):
    if a[i] == "-1" and  all(a[j] in '13' for j in f(i)):
        a[i] = "4"
print(*a[1:], sep="\t")