def f(a,b):
    if a == b:
        return 1
    if a > b :
        return 0
    return f(a + 3,b) + f(a * 3,b)

k = 0
for i in range(2,99, 2):
    if f(3,i) > 0:
        k +=1
print(k)