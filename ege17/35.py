k = []
for i in range(1476,7039 + 1):
    if  ((i % 2 == 0) and (i % 16 != 0)) and (i//10 % 10 >= 4):
        k.append(i)
print(len(k),(min(k) + max(k)) // 2)