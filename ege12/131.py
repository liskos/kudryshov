s = 9 * "4" + 12 * "5"
while "444" in s or "888" in s:
    if "444" in s:
        s = s.replace("444","8",1)
    while "555" in s:
        s = s.replace("555","8",1)
    while "888" in s:
        s = s.replace("888","3",1)

print(s)