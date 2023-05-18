a= []
for i in range(-9563,-3102 + 1 ):
    if abs(i) % 7 == 0 and (abs(i) % 11 != 0 and abs(i) % 23 != 0) and i % 10 != 8:
        a.append(i)
print(len(a),max(a))
        