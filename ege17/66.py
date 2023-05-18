a = []
for i in range(333666,666999 + 1):
    s = str(i)
    if (s.count("7") >= 2) and (i % 17 == 0) :
        a.append(i)
print(max(a),len(a))
