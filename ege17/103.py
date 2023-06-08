

a = []
for i in range(10,9999+1):
    if (i % 2 == 1) and (i % 3 == 0) and (i % 11 == 0) and bin(i)[2:].count("0") == 5:
        a.append(i)

print(len(a),max(a))