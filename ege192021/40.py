a = ["-1"] * 200
for i in range(200):
    if i >= 33:
        a[i] = "0"
for i in range(34):
    if a[i] == "-1" and  any((a[i+3] == '0',a[i*2] == '0')):
        a[i] = "1"
for i in range(34):
    if a[i] == "-1" and  all((a[i+3] == '1',a[i*2] == '1')):
        a[i] = "2"
for i in range(34):
    if a[i] == "-1" and  any((a[i+3] == '2', a[i*2] == '2')):
        a[i] = "3"
for i in range(34):
    if a[i] == "-1" and  all((a[i+3] in "13",a[i*2] in '13')):
        a[i] = "4"
print(*a[1:], sep="\t")