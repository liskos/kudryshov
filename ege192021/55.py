a = [["-1"] * 400 for i in range(400) ]
for x in range(400):
    for y in range(400):
        if x + y >= 95:
            a[x][y] = "0"
for x in range(96):
    for y in range(96):
        if a[x][y] == "-1":
            if any((a[i][j] == "0" for i,j in [(x+1,y),(x,y+1),(x*4,y),(x,y*4)])):
                a[x][y] = "1"
for x in range(96):
    for y in range(96):
        if a[x][y] == "-1":
            if all((a[i][j] == "1" for i,j in [(x+1,y),(x,y+1),(x*4,y),(x,y*4)])):
                a[x][y] = "2"
for x in range(96):
    for y in range(96):
        if a[x][y] == "-1":
            if any((a[i][j] == "2" for i,j in [(x+1,y),(x,y+1),(x*4,y),(x,y*4)])):
                a[x][y] = "3"
for x in range(96):
    for y in range(96):
        if a[x][y] == "-1":
            if all((a[i][j] in "13" for i,j in [(x+1,y),(x,y+1),(x*4,y),(x,y*4)])):
                a[x][y] = "4"



for i in range(1,400):
    print(*a[i][1:], sep="\t")