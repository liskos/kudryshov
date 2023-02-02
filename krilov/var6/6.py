k = 0
for x in range(-1000,1000):
    for y in range (-1000,1000):
        if (1 / 3 ** 0.5) * x < y < (-1 / 3 ** 0.5) * x + 123 and 0 < x <= 106:
            k +=1
print(k)
