s = "1" + 50 * "23"
while "123" in s or "1" in s:
    if "123" in s:
        s = s.replace("123","23231",1)
    elif "1" in s:
        s = s.replace("1","23",1)

print(s.count("2"))
