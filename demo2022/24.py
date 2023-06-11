import sys
sys.stdin = open("24_4710.txt")
s = input()
a =[]
s = s.replace("A","G")
s = s.replace("O","G")
s = s.replace("C","S")
s = s.replace("D","S")
s = s.replace("F","S")
s = s.replace("GG","G G")
s = s.replace("SS","S S")
s = s.replace("GS","X")
s = s.replace("S"," ")
s = s.replace("G"," ")


print(max(map(len,s.split())))