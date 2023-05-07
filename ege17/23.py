a = []
for i in range (3232,8299 + 1):
    if ((i % 2 == 0) or (i % 7 == 0))  and (i % 15 != 0) and (i % 28 != 0) and (i % 41 != 0):
        a.append(i)
print(min(a),max(a))