s = "3" + 57 * "5"
while "25" in s or "355" in s or "4555" in s:
    if "25" in s :
        s = s.replace("25","3",1)
    if "355" in s:
        s = s.replace("355", "4", 1)
    if "4555" in s :
        s = s.replace("4555","2",1)
print(s)
