k = []
for i in range(2461,9719 + 1):
    if  ((i % 100 != 1) and (i % 100 != 9)) and (3 <= i % 10 <= 7):
        k.append(i)
print(len(k),(max(k)))