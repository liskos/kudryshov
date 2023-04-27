def f(n):
    b = []
    if n % 2 == 0:
        b.append(n // 2)
    else:
        b.append(n - 2)
    if n % 3 == 0:
        b.append(n  // 3)
    else :
        b.append(n - 3)
    return b


a = ["-1"] * 200
for i in range(200):
    if i <= 2:
        a[i] = "0"
for i in range(100):
    if a[i] == "-1" and any(a[j] == '0' for j in f(i)):
        a[i] = "1"
for i in range(100):
    if a[i] == "-1" and all(a[j] == '1' for j in f(i)):
        a[i] = "2"
for i in range(100):
    if a[i] == "-1" and any(a[j] == '2' for j in f(i)):
        a[i] = "3"
for i in range(100):
    if a[i] == "-1" and all(a[j] in '13' for j in f(i)):
        a[i] = "4"
print(*a[1:], sep="\t")
