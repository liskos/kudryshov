s = 95 * "1" + 31 * "7"
while "1111" in s :
    s = s.replace("1111","7",1)
    s = s.replace("77","1",1)
print(s)
