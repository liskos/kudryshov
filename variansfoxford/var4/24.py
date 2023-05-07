import sys
sys.stdin = open("24.txt")

a = input()

a = a.replace("A","G")
a = a.replace("B","S")
a = a.replace("C","S")
a = a.replace("D","S")
a = a.replace("E","G")
a = a.replace("GS","X")
a = a.replace("G"," ")
a = a.replace("S"," ")


print(max(map(len,a.split())))


