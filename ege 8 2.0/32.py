a = set()
b = set ()
for s1 in "ABCD":
    for s2 in "ABCD":
        for s3 in "ABCD":
            s = s1 + s2 + s3
            if ("BC" not in s) and ("CB" not in s):
                a.add(s)
for x in a:
    if x.count("A") == 0:
        b.add(x)
    elif ("AD" in x) or ("DA" in x):
        b.add(x)
for x in b:
    if x.count("A") >= 2:
        print(x)

print(len(b))
print(b)




