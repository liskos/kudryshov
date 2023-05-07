for i in range(1037799,10**10,2023):
    s = str(i)
    if s[0] == "1" and s[2:6] == "3616" and s[-1]=="7":
        print(s,i // 2023)