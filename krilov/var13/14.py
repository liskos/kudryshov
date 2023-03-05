for x in "0123456789abcde":
    s1 = "135" + x + "7"
    s2 = "7" + x + "531"
    s  = int(s1,15) + int(s2,15)
    if s % 14 == 0:
        print(x)
        break
print(s // 14)