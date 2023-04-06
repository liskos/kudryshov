a = [["-1"] * 140 for i in range(140)]

for x in range(1,140):
    for y in range(1, 140):
        if x + y >= 75:
            a[x][y] = "0"
for x in range(1,70):
    for y in range(1, 70):
        if a[x][y] == "-1" and (a[x + 1][y] == "0" or a[x][y+1] == "0" or a[x * 2][y] == "0" or a[x][y*2] == "0"):
            a[x][y] = "1"
for x in range(1,70):
    for y in range(1, 70):
        if a[x][y] == "-1" and a[x + 1][y] == "1" and a[x][y + 1] == "1" and a[x * 2][y] == "1" and a[x][y * 2] == "1":
                a[x][y] = "2"
for x in range(1,70):
    for y in range(1, 70):
        if a[x][y] == "-1" and (a[x + 1][y] == "2" or a[x][y + 1] == "2" or a[x * 2][y] == "2" or a[x][y * 2] == "2"):
                a[x][y] = "3"
for x in range(1,70):
    for y in range(1, 70):
        if a[x][y] == "-1" and (a[x + 1][y] in "13"  and  a[x][y + 1] in "13" and a[x * 2][y] and "13" and a[x][y * 2] in "13"):
                a[x][y] = "4"


for i in range(1,75):
    print(*a[i][1:], sep="\t")

