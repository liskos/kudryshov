b = []
k = 0
for i in range(21005, 147870 + 1):
    if ("1" not in str(i)) and int(max(str(i))) - int(min(str(i))) < 4:
        b.append(i)
        k+=1
print(b[::-1],k)
print(len(b))