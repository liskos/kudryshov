import sys
sys.stdin = open("24.txt")
s = input()

s1 = ""
for i in s:
    if i.isdigit():
        s1 += str(int(i) % 2)
    else:
        s1 += "*"
s2 = s1.replace("0","1")
m = max(map(len,s2.split("1")))

for n in range(0,m + 1):
    if "0"+n * "*" + "1" in s1:
        print(n+2)
    elif "1"+n * "*" + "0" in s1:
        print(n+2)

