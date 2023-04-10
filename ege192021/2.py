<<<<<<< HEAD
a = [[""] * 200 for _ in range(200)]
for i in range(200):
    for j in range(200):
        if i + j >= 83:
            a[i][j] = "0"
for i in range(100):
    for j in range(100):
        if a[i][j] == "" and (a[i+1][j] == "0" or a[i][j+1] == "0" or a[i*2][j] == "0" or a[i][j*2] == "0") :
            a[i][j] = "1"
for i in range(100):
    for j in range(100):
        if a[i][j] == "" and (a[i+1][j] == "1" and a[i][j+1] == "1" and a[i*2][j] == "1" and a[i][j*2] == "1") :
            a[i][j] = "2"
for i in range(100):
    for j in range(100):
        if a[i][j] == "" and (a[i+1][j] == "2" or a[i][j+1] == "2" or a[i*2][j] == "2" or a[i][j*2] == "2") :
            a[i][j] = "3"
for i in range(100):
    for j in range(100):
        if a[i][j] == "" and ((a[i+1][j] == "1" or a[i+1][j] == "3")  and (a[i][j+1] == "1" or a[i][j+1] == "3")
                              and (a[i*2][j] == "1" or a[i*2][j] == "3") and (a[i][j*2] == "1" or a[i][j*2] == "3")) :
            a[i][j] = "4"



for i in range(1,100):
     print(*a[i][1::], sep="\t")
=======
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
>>>>>>> origin/master
