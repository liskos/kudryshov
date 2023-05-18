a = []
for i in range(1346,7996 + 1):
    if (i % 3 == 0) and (i % 13 != 0) :
        a.append(i)
print(len(a),sum(a))
print(a)
