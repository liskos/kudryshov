k = 0
for i in range(100000, 999999+1):
    s1,s2,s3,s4,s5,s6 = str(i)
    if s1 > s2 > s3 > s4 > s5 > s6 and int(s2) % 2 == int(s4) % 2 == int(s6) % 2 and int(s1) % 2 == int(s3) % 2 == int(s5) % 2 and int(s2) % 2 != int(s3) % 2 :
        k += 1
print(k)