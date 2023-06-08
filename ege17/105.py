a = []
for i in range(31,2047+1):
    if (i % 2 == 0) and (i % 10 != 0) and bin(i)[2:].count("1") == 5:
        a.append(i)

print(len(a),max(a))