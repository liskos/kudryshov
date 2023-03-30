a = [[""] * 300 for _ in range(300)]
for x in range(0,300):
    for y in range(0,300):
        if x*y >= 144:
            a[x][y] = "0"
for x in range(0,145):
    for y in range(0,145):
        if a[x][y] == "" and (a[x + 1][y] == "0" or a[x * 2][y] == "0" or a[x][y+1] == "0" or a[x][y*2] == "0") :
            a[x][y] = "1"
for x in range(0,145):
    for y in range(0,145):
        if a[x][y] == "" and (a[x + 1][y] == "1" and a[x * 2][y] == "1" and a[x][y+1] == "1" and a[x][y*2] == "1") :
            a[x][y] = "2"
for x in range(0,145):
    for y in range(0,145):
        if a[x][y] == "" and (a[x + 1][y] == "2" or a[x * 2][y] == "2" or a[x][y+1] == "2" or a[x][y*2] == "2") :
            a[x][y] = "3"
for x in range(0,145):
    for y in range(0,145):
        if a[x][y] == "" and ((a[x + 1][y] == "1" or a[x + 1][y] == "3" ) and
                              (a[x * 2][y] == "1" or a[x * 2][y] == "3") and
                              (a[x][y+1] == "1" or a[x][y+1] == "3") and (a[x][y*2] == "1" or a[x][y*2] == "3" )):
            a[x][y] = "4"






for s in a[1:]:
    print(*s[1:], sep= "\t")
