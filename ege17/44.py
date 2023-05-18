a = []
for i in range (3912,9193 + 1):
    if (sum(map(int, str(i))) % 9 == 0) and (not(i%16 == 1 and i//16%16 == 2 )) :
        a.append(i)
print(len(a),max(a))