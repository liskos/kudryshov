from fnmatch import *
for x in range(999,10**9,999):
    if fnmatch(str(x),"13???57?9"):
        print(x,x//999)
