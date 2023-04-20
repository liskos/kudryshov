a = ["-1"] * 200
for i in range(200):
    if i >= 25:
        a[i] = "0"
for i in range(26):
    if a[i] == "-1" and  any(a[i] == '0' for i in [(i+2),(i*2)]):
        a[i] = "1"
for i in range(26):
    if a[i] == "-1" and  all(a[i] == '1' for i in [(i+2),(i*2)]):
        a[i] = "2"
for i in range(26):
    if a[i] == "-1" and  any(a[i] == '2' for i in [(i+2),(i*2)]):
        a[i] = "3"
for i in range(26):
    if a[i] == "-1" and  all(a[i] in '13' for i in [(i+2),(i*2)]):
        a[i] = "4"
print(*a[1:], sep="\t")