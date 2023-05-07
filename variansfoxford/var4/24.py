import sys
sys.stdin = open("24.txt")

a = input()

a = a.replace("AB","XX")
a = a.replace("AC","XX")
a = a.replace("AD","XX")
a = a.replace("EB","XX")
a = a.replace("EC","XX")
a = a.replace("ED","XX")
a = a.replace("XA","X A")
a = a.replace("XB","X B")
a = a.replace("XC","X C")
a = a.replace("XD","X D")
a = a.replace("XE","X E")
a = a.replace("AX","A X")
a = a.replace("BX","B X")
a = a.replace("CX","C X")
a = a.replace("DX","D X")
a = a.replace("EX","E X")
print(max(map(len,a.split())))

