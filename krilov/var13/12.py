a = "1" + 25 * "5"
while "15" in a or "1" in a:
    if "15" in a:
        a = a.replace("15","5551",1)
    else :
        if "1" in a:
            a = a.replace("1","5",1)

print(len(a))