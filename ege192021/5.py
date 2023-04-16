a = [["-1"] * 150 for i in range(150) ]
for x in range(150):
    for y in range(150):
        if x + y >= 57:
            a[x][y] = "0"
for x in range(58):
    for y in range(58):
        if a[x][y] == "-1":
            if any((a[i][j] == "0" for i,j in [(x+1,y),(x,y+1),(x*2,y),(x,y*2)])):
                a[x][y] = "1"
for x in range(58):
    for y in range(58):
        if a[x][y] == "-1":
            if all((a[i][j] == "1" for i,j in [(x+1,y),(x,y+1),(x*2,y),(x,y*2)])):
                a[x][y] = "2"
for x in range(58):
    for y in range(58):
        if a[x][y] == "-1":
            if any((a[i][j] == "2" for i,j in [(x+1,y),(x,y+1),(x*2,y),(x,y*2)])):
                a[x][y] = "3"
for x in range(58):
    for y in range(58):
        if a[x][y] == "-1":
            if all((a[i][j] in "13" for i,j in [(x+1,y),(x,y+1),(x*2,y),(x,y*2)])):
                a[x][y] = "4"



for i in range(1,150):
    print(*a[i][1:], sep="\t")