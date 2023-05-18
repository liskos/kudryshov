a = []
for i in range(1705,7474 + 1):
    if (i % 11 == 0) and (i % 19 != 0) :
        a.append(i)
print(len(a),sum(a))
print(a)
