import sys
sys.stdin = open("KIM_0001234567_24.txt")

a = input()

a = a.replace("CFE","X")
a = a.replace("FCE","X")
a = a.replace("C"," ")
a = a.replace("D"," ")
a = a.replace("E"," ")
a = a.replace("F"," ")
print(max(map(len,a.split())))
