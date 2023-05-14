k=[]
for s1 in ["", "0","1","2","3","4","5","6","7","8","9"]:
    for s2 in "0123456789":
        for s3 in "0123456789":
            s = "12" + s2 + s3 +"1" + s1 + "56"
            if int(s) % 317 == 0:
                k.append(int(s))
k = sorted(k)
for i in k:
    print(i,i //317)



