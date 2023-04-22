a = [["-1"] * 200 for i in range(200) ]
for x in range(200):
    for y in range(200):
        if x + y >= 45:
            a[x][y] = "0"
for x in range(45):
    for y in range(45):
        if a[x][y] == "-1":
            if any((a[i][j] == "0" for i,j in [(x+2,y),(x,y+2),(x*3,y),(x,y*3)])):
                a[x][y] = "1"
for x in range(45):
    for y in range(45):
        if a[x][y] == "-1":
            if all((a[i][j] == "1" for i,j in [(x+2,y),(x,y+2),(x*3,y),(x,y*3)])):
                a[x][y] = "2"
for x in range(45):
    for y in range(45):
        if a[x][y] == "-1":
            if any((a[i][j] == "2" for i,j in [(x+2,y),(x,y+2),(x*3,y),(x,y*3)])):
                a[x][y] = "3"
for x in range(45):
    for y in range(45):
        if a[x][y] == "-1":
            if all((a[i][j] in "13" for i,j in [(x+2,y),(x,y+2),(x*3,y),(x,y*3)])):
                a[x][y] = "4"



for i in range(1,200):
    print(*a[i][1:], sep="\t")