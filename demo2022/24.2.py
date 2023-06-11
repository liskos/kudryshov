import sys
sys.stdin = open("24_4710.txt")
s = input()

def f(s):
    s = s.replace("A", "G")
    s = s.replace("O", "G")
    s = s.replace("C", "S")
    s = s.replace("D", "S")
    s = s.replace("F", "S")
    return "SG" * (len(s) // 2) + "S" * (len(s) % 2) == s


t = ""
m = 0
for i in s:
    t += i
    while not f(t):
        t = t[1:]
    if len(t) % 2 == 0:
        m = max(m , len(t))
print(m)
