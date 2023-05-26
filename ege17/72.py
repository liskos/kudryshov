b = []
for i in range(2848, 109499 + 1):
    a = list(str(i))
    if '0' in a:
        a = a.pop(0)
    if '1' in a:
        a = a.pop(1)
    if '2' in a:
        a = a.pop(2)
    if '3' in a:
        a = a.pop(3)
    if '4' in a:
        a = a.pop(4)
    if '5' in a:
        a = a.pop(5)

    if "9" in str(i) and sum(map(int,a)):
        b.append(i)
        print(sum(map(int,a)),a)

print(len(b))
print(a)