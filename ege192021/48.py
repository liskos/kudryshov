def f(n):
    b = []
    if n + 1 <= 72:
        b.append(n+1)
    if n * 2 <= 72:
        b.append(n * 2)
    if n * 3 <= 72:
        b.append(n * 3)
    return b


a = ["-1"] * 200
for i in range(200):
    if 43 <= i <= 72:
        a[i] = "0"
for i in range(73):
    if a[i] == "-1" and  any(a[j] == '0' for j in f(i)):
        a[i] = "1"
for i in range(73):
    if a[i] == "-1" and  all(a[j] in '1' for j in f(i)):
        a[i] = "2"
for i in range(73):
    if a[i] == "-1" and  any(a[j] == '2' for j in f(i)):
        a[i] = "3"
for i in range(73):
    if a[i] == "-1" and  all(a[j] in '13' for j in f(i)):
        a[i] = "4"
print(*a[1:], sep="\t")