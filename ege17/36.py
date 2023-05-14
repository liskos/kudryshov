k = []
for i in range(2476,7857 + 1):
    if  ((i % 2 == 0) and (i % 8 != 0)) and (i // 100 % 10 <= 7):
        k.append(i)
print(len(k),(min(k) + max(k)) // 2)