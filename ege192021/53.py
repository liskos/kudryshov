a = ["-1"] * 200
for i in range(200,1,-1):
    if i <= 10:
        a[i] = "0"
for i in range(100,1,-1):
    if a[i] == "-1" and  any(a[j] == '0' for j in [(i-1),(i//2)]):
        a[i] = "1"
for i in range(100,1,-1):
    if a[i] == "-1" and  all(a[j] == '1' for j in [(i-1),(i//2)]):
        a[i] = "2"
for i in range(100,1,-1):
    if a[i] == "-1" and  any(a[j] == '2' for j in [(i-1),(i//2)]):
        a[i] = "3"
for i in range(100,1,-1):
    if a[i] == "-1" and  all(a[j] in '13' for j in [(i-1),(i//2)]):
        a[i] = "4"
print(*a[1:], sep="\t")