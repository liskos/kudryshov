a = []
for i in range(2020,647038 + 1):
     if (sum(map(int, str(i))) < 10) and (min(str(i)) != str(i)[0] and min(str(i)) != str(i)[1] and min(str(i)) != str(i)[2]):
         a.append(i)
print(a)
print(sum(a) / len(a))
print(len(a))