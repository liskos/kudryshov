a = {"0" * (8 - len(bin(i)[2:])) + bin(i)[2:]  for i in range(0,256)}
p = {i for i in a if i[:2] == "11"}
q = {i for i in a if i[-1] == "0"}
b = a.copy()
for i in b:
    a.remove(i)
    c = all((x in a) or ((x not in p) and (x not in q)) for x in b)
    if not  c:
        a.add(i)

print(len(a))

