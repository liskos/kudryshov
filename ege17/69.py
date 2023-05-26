b = []
for i in range(1388, 63252 + 1):
    if (i % 12 != 0) and ("7" in str(i) or "4" in str(i)):
        b.append(i)

print(max(b),len(b))
