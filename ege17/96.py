a = []
for i in range(-999,999+1):
    if abs(i) % 16 == 15 and abs(i) % 12 != 0 and abs(i) % 13 != 0:
        a.append(abs(i))
print(len(a), max(a))