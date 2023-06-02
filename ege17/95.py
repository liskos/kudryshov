a = []
for i in range(-5000,5000):
    if abs(i) % 16 == 11 and abs(i) % 6 != 0 and abs(i) % 5 == 0 and abs(i) % 7 == 0 :
        a.append(abs(i))
print(len(a),max(a))