s = 2018 * "1" + 2019 * "2"
while "111" in s or "222" in s :
    s = s.replace("111","2",1)
    s = s.replace("222","1",1)
print(s)
