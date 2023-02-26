import sys

sys.stdin = open("17.txt")
a = []
m = []
for i in range(5000):
    a.append(int(input()))
mina = 10000
for i in range(5000):
    if str(a[i])[-1] == "7":
        mina = min(a[i],mina)

for i in range(4999):
    if ((str(a[i])[-1] == "7" and str(a[i+1])[-1] != "7") or (str(a[i])[-1] != "7" and str(a[i+1])[-1] == "7")) and ((a[i] + a[i+1]) ** 2 >= mina ** 2):
        m.append(a[i] + a[i+1])
print(len(m), max(m) ** 2, min(m) ** 2)
