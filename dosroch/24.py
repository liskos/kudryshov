import sys
sys.stdin = open("24.txt")
s = ""
for i in range(1000):
    s += input()
k = 0
for p in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if "Q" + p + p + "A" in s:
        k += 1

print(k)
