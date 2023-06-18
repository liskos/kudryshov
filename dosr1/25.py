import fnmatch
for x in range(273,10**8,273):
    if fnmatch.fnmatch(str(x),"12??36*1"):
        print(x,x//273)