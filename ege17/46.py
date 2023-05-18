a = []
for i in range(-7018, -3790 + 1):
    if abs(i) % 6 == 0 and (abs(i) % 7 != 0 and abs(i) % 19 != 0) and i % 10 != 2:
        a.append(i)
print(len(a), min(a))
