b = []
for i in range(2848, 109499 + 1):
    if "9" in str(i) and sum([int(x) for x in str(i) if int(x) > 5 ]) % 3 == 0:
        b.append(i)

print(len(b))
c = [x for x in b if str(x)[0] == "8"]
print(max(c))