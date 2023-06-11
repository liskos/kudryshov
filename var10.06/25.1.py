for i in range(130136*999,10**9, 999):
    s = str(i)
    if s[:2] == "13" and s[5:7] == "57" and s[-1] == "9":
        print(s,i//999)