s = 9 * "8" + 12 * "5"
while "555" in s or "888" in s:
    while "555" in s:
        s = s.replace("555","8",1)
    while "888" in s :
        s = s.replace("888","2",1)

print(s)
