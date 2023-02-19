import sys
sys.stdin = open("24var03.txt")

s = input()
s = s.replace("AB","X")
s1 = ""
for i in s:
    s1 += i
    if s1.count("X") == 21:
        break
print(s1)
m = len(s1)
t = ""
for i in range(len(s1),len(s)):
    t += s[i]
    if "X" in t :
        s1 += t
        t = ""
        s1 = s1[1:]
        while s1[0] != "X":
            s1 = s1[1:]
        m = min(m,len(s1))
print(m + 21)