a = []
for i in range(1753,7420 + 1):
    if (i % 11 == 0) and (i % 13 != 0) :
        a.append(i)
print(len(a),sum(a))
print(a)
