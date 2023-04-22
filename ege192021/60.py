a = [["-1"] * 600 for i in range(600) ]
for x in range(600):
    for y in range(600):
        if x + y >= 125:
            a[x][y] = "0"
for x in range(126):
    for y in range(126):
        if a[x][y] == "-1":
            if any((a[i][j] == "0" for i,j in [(x+1,y),(x,y+1),(x*4,y),(x,y*4)])):
                a[x][y] = "1"
for x in range(126):
    for y in range(126):
        if a[x][y] == "-1":
            if all((a[i][j] == "1" for i,j in [(x+1,y),(x,y+1),(x*4,y),(x,y*4)])):
                a[x][y] = "2"
for x in range(126):
    for y in range(126):
        if a[x][y] == "-1":
            if any((a[i][j] == "2" for i,j in [(x+1,y),(x,y+1),(x*4,y),(x,y*4)])):
                a[x][y] = "3"
for x in range(126):
    for y in range(126):
        if a[x][y] == "-1":
            if all((a[i][j] in "13" for i,j in [(x+1,y),(x,y+1),(x*4,y),(x,y*4)])):
                a[x][y] = "4"



for i in range(1,600):
    print(*a[i][1:], sep="\t")