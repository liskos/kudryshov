import sys
sys.stdin = open("24_7600.txt")

s = input()

s = s.replace("QR","Q R")
s = s.replace("QS","Q S")
s = s.replace("QQ","Q Q")
s = s.replace("RQ","R Q")
s = s.replace("RS","R S")
s = s.replace("RR","R R")
s = s.replace("SQ","S Q")
s = s.replace("SR","S R")
s = s.replace("SS","S S")
print(len(max(map(str,s.split()))))