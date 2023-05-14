k = []
for i in range(3905,7998 + 1):
    if  ((i % 10 != 0) and (i % 10 != 5)) and (2 <= i % 100 <= 6):
        k.append(i)
print(len(k),(min(k)))