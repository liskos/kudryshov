s = "1" + 80 * "0"
while "10" in s or "1" in s :
    if "10" in s :
        s = s.replace("10","001",1)
    else:
        s = s.replace("1","000",1)

print(s.count("0"))