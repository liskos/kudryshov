i = 15
a = []
while i < 2000000:
    if len(set(str(i))) < len(str(i)):
        a.append(i)
    i = i * 2
print(len(a))
print(max(a) - min(a))
print(a)