a = []
for i in range(64,1024+1):
    if (i % 2 == 0) and (i % 8 == 0) and (i % 5 != 0) and bin(i)[2:].count("1") == 3:
        a.append(i)

print(len(a),max(a))