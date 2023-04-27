a = [["-1"] * 300 for i in range(300) ]
for x in range(300):
    for y in range(300):
        if x + y >= 99:
            a[x][y] = "0"
for x in range(99):
    for y in range(99):
        if a[x][y] == "-1":
            if any((a[i][j] == "0" for i,j in [(x+1,y),(x,y+1),(x*3,y),(x,y*3)])):
                a[x][y] = "1"
for x in range(99):
    for y in range(99):
        if a[x][y] == "-1":
            if all((a[i][j] == "1" for i,j in [(x+1,y),(x,y+1),(x*3,y),(x,y*3)])):
                a[x][y] = "2"
for x in range(99):
    for y in range(99):
        if a[x][y] == "-1":
            if any((a[i][j] == "2" for i,j in [(x+1,y),(x,y+1),(x*3,y),(x,y*3)])):
                a[x][y] = "3"
for x in range(99):
    for y in range(99):
        if a[x][y] == "-1":
            if all((a[i][j] in "13" for i,j in [(x+1,y),(x,y+1),(x*3,y),(x,y*3)])):
                a[x][y] = "4"



for i in range(1,300):
    print(*a[i][1:], sep="\t")