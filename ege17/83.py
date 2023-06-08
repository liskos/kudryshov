a = []
for i in range(1111, 9999 + 1):
    if i % sum(map(int, str(i))) == 0 and i % :
        a.append(i)
print(len(a), max(a))
