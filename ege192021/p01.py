a = [""] * 100
for i in range(100):
    if i >= 29:
        a[i] = "0"
for i in range(30):
    if a[i] == "" and  (a[i*2] == "0" or  a[i+1] == "0"):
        a[i] = "1"
for i in range(30):
    if a[i] == "" and  (a[i*2] == "1" and  a[i+1] == "1"):
        a[i] = "2"
for i in range(30):
    if a[i] == "" and  (a[i*2] == "2" or a[i+1] == "2"):
        a[i] = "3"
for i in range(30):
    if a[i] == "" and ((a[i * 2] == "1" or a[i * 2] == "3") and (a[i + 1] == "1" or a[i + 1] == "3")):
        a[i] = "4"

print(*a[1::], sep="\t")

for i in range(50):
    print(i, a[i])