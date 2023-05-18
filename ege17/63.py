a = []
for i in range(1840,9052 + 1):
    if (i % 7 == 0) and (i % 23 != 0) :
        a.append(i)
print(len(a),sum(a))

