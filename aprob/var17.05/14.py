for x in "0123456789ABCDE":
    s1 = "99658" + x + "29"
    s2 = "102" + x + "023"
    s = int(s1,15) + int(s2,15)
    if s % 14 == 0:
        print(x,s)
print((int("99658E29",15) + int("102E023",15))//14)