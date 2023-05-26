b = []
for i in range(2079, 43167 + 1):
    if (i % 7== 0) and ("0" in str(i) and "2" in str(i) and "5" in str(i)):
        b.append(i)

print(min(b),len(b))
