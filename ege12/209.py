s = 63 * "1" + 61 * "2"
while "111" in s :
    s = s.replace("111","22",1)
    s = s.replace("2222","1",1)
print(s)
