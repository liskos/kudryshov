s = 197 * "4"
while "4444" in s or "777" in s :
    if "4444" in s:
        s = s.replace("4444","77",1)
    else :
        s = s.replace("777","44",1)

print(s)