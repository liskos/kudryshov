a = ["-1"] * 999
for x in range(1,999):
    if x >= 351:
        a[x] = "0"

for x in range (1,351):
    if a[x] == "-1" and any(a[i] =="0" for i in [(x+1),(x+4),(x*2)]):
        a[x] = "1"
for x in range (1,351):
    if a[x] == "-1" and all(a[i] == "1" for i in [(x+1),(x+4),(x*2)]):
        a[x] = "2"

for x in range (1,351):
    if a[x] == "-1" and any(a[i] =="2" for i in [(x+1),(x+4),(x*2)]):
        a[x] = "3"

for x in range (1,351):
    if a[x] == "-1" and all(a[i] in "13" for i in [(x+1),(x+4),(x*2)]):
        a[x] = "4"



print(*a[1:], sep="\t")

