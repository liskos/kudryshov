b = []
for i in range(2894, 174882 + 1):
    if (i % 10 == 8) and sum(map(int,str(i))) > 22:
        b.append(i)

print(len(b))
print(b[12])
