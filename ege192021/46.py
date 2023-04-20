a = ["-1"] * 200
for i in range(200):
    if 45 <= i <= 112:
        a[i] = "0"
for i in range(46):
    if a[i] == "-1" and  any(a[i] == '0' for i in [(i+2),(i*3)]):
        a[i] = "1"
for i in range(46):
    if a[i] == "-1" and  all(a[i] == '1' for i in [(i+2),(i*3)]):
        a[i] = "2"
for i in range(46):
    if a[i] == "-1" and  any(a[i] == '2' for i in [(i+2),(i*3)]):
        a[i] = "3"
for i in range(46):
    if a[i] == "-1" and  all(a[i] in '13' for i in [(i+2),(i*3)]):
        a[i] = "4"
print(*a[1:], sep="\t")