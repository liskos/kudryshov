a = []
for i in range(15,1000+1):
    if (i % 7 == 6) and (i % 32 == 0):
        a.append(i)

print(len(a),max(a))