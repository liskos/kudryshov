b = []
for i in range(1031, 125888 + 1):
    if (i % 10 != 5) and (i**0.5) == int(i**0.5):
        b.append(i)
    if (i % 10 != 5) and (i**0.5) == int(i**0.5) and i % 100 == 36:
        print(i)

print(len(b))

