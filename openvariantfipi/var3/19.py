a = ["-1"] * 350
for i in range(350):
    if i >= 43:
        a[i] = "0"
for i in range(43):
    if a[i] == "-1" and any(a[j] == '0' for j in [(i + 1), (i + 4),(i * 3)]):
        a[i] = "1"
for i in range(43):
    if a[i] == "-1" and all(a[j] == '1' for j in [(i + 1), (i + 4),(i * 3)]):
        a[i] = "2"
for i in range(43):
    if a[i] == "-1" and any(a[j] == '2' for j in [(i + 1), (i + 4),(i * 3)]):
        a[i] = "3"
for i in range(43):
    if a[i] == "-1" and all(a[j] in '13' for j in [(i + 1), (i + 4),(i * 3)]):
        a[i] = "4"
print(*a[1:], sep="\t")