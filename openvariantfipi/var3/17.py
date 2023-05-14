import sys

sys.stdin = open("1_17.txt")

b = []
a = [input() for i in range(4403)]
m = max([int(a[i]) for i in range(4403) if len(a[i]) == 2])
b = [int(a[i]) + int(a[i+1]) for i in range(4402) if ((len(a[i]) == 2 and len(a[i+1]) != 2) or (len(a[i]) != 2 and
                                            len(a[i+1]) == 2)) and ((int(a[i]) + int(a[i+1])) % m == 0) ]

print(len(b),max(b))


