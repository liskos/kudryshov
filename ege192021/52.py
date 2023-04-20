a = ["-1"] * 2500
for i in range(2500):
    if i >= 1000:
        a[i] = "0"
for i in range(1001):
    if a[i] == "-1" and  any(a[j] == '0' for j in [(i+100),(i*2)]):
        a[i] = "1"
for i in range(1001):
    if a[i] == "-1" and  all(a[j] == '1' for j in [(i+100),(i*2)]):
        a[i] = "2"
for i in range(1001):
    if a[i] == "-1" and  any(a[j] == '2' for j in [(i+100),(i*2)]):
        a[i] = "3"
for i in range(1001):
    if a[i] == "-1" and  all(a[j] in '13' for j in [(i+100),(i*2)]):
        a[i] = "4"
print(*a[1:], sep="\t")