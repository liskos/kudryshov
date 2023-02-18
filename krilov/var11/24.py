import sys
sys.stdin = open("24var09-13.txt")

s = input()

s = s.replace("XZ","X Z")
s = s.replace("ZY","Z Y")
s = s.replace("YZ", "Y Z")
s = s.replace("ZX", "Z X")
s = s.replace("ZZ","Z Z")
print (max(map(len,s.split())))
