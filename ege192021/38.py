def f(x):
    a = [x+1,x+3,x*3]
    b = [i for i in a if i % 2 != 0]
    return b
a = ["-1"] * 200
for i in range(200):
    if i >= 51:
        a[i] = "0"
for i in range(52):
    if a[i] == "-1" and  any(a[i] == '0' for i in f(i)):
        a[i] = "1"
for i in range(52):
    if a[i] == "-1" and  all(a[i] == '1' for i in f(i)):
        a[i] = "2"
for i in range(52):
    if a[i] == "-1" and  any(a[i] == '2' for i in f(i)):
        a[i] = "3"
for i in range(52):
    if a[i] == "-1" and  all(a[i] in '13' for i in f(i)):
        a[i] = "4"
print(*a[1:], sep="\t")