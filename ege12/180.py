s = "5" * 500
while "555" in s or "333" in s:
    if "555" in s:
        s = s.replace("555","3",1)
        print(s.count("3"))
    else:
        s = s.replace("333","5",1)
        
print(s)