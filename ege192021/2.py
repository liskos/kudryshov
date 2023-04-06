a = [["-1"] * 200 for i in range(200)]
for x in range(200):
    for y in range(200):
        if x + y >= 83:
            a[x][y] = "0"

for x in range(83):
    for y in range(83):
        if a[x][y] == "-1" and any([a[i][j] == "0" for i, j in ((x+1,y), (x,y + 1), (x*2,y), (x,y*2))]):
            a[x][y] = "1"
for x in range(83):
    for y in range(83):
        if a[x][y]=="-1" and all((a[x+1][y] == "1" , a[x][y+1] == "1" , a[x*2][y] == "1", a[x][y*2] == "1")):
            a[x][y] = "2"
for x in range(83):
    for y in range(83):
        if a[x][y]=="-1" and any((a[x+1][y] == "2" , a[x][y+1] == "2" , a[x*2][y] == "2", a[x][y*2] == "2")):
            a[x][y] = "3"
for x in range(83):
    for y in range(83):
        if a[x][y]=="-1" and all((a[x+1][y] in "13" , a[x][y+1] in "13" , a[x*2][y] in "13", a[x][y*2] in "13")):
            a[x][y] = "4"

for i in range(1,200):
    print(*a[i][1:],sep="\t")
