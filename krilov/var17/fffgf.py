a = [[4, 6, 9, 7], [4, 6, 8, -9], [5, 7, 8, 4]]
print(a)
for s in a[1:]:
    print(*s[1:],sep = "\t")