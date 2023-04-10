a = ["" * 999]
for x in range(1,999):
    if x >= 351:
        a[x] = "0"

for x in range (1,351):
    if a[x] == "" and (a[x+1] == "0" or a[x + 4] == "0" or a[x*2] == "0"):
        a[x] = "1"
for x in range (1,351):
    if a[x] == "" and (a[x+1] == "0" or a[x + 4] == "0" or a[x*2] == "0"):
        a[x] = "1"

for x in range (1,351):
    if a[x] == "" and (a[x+1] == "1" and a[x + 4] == "0" and a[x*2] == "1"):
        a[x] = "2"

for x in range (1,351):
    if a[x] == "" and (a[x+1] == "2" or a[x + 4] == "2" or a[x*2] == "2"):
        a[x] = "3"
for x in range (1,351):
    if a[x] == "" and ((a[x+1] == "3" or a[x+1] == "1" ) and (a[x + 4] == "3" or a[x + 4] == "1")  and  (a[x*2] == "3" or a[x*2] == "1")):
        a[x] = "4"



print(*a[x][1:], sep="\t")

