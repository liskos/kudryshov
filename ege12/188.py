s = 121 * "563"
while "56" in s or "1111" in s:
    s = s.replace("56","3",1)
    s = s.replace("3333", "3", 1)
print(s)