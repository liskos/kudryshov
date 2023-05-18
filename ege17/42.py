a = []
for i in range (2495,7083 + 1):
    if ((i % 16 == 10 and i // 16 % 16 == 1) or (i % 16 == 15 and i // 16 % 16 == 1)) and  ((i % 5 != 0) and (i % 9 != 0)) :
        a.append(i)
print(len(a),min(a))