k = 0
for i in range(2,999):
    b = bin(i)[2:]
    b = b + b[-2]
    b = b + b[1]
    b = int(b,2)
    if 150 <= b <= 200:
        k+=1
        print(i,k)

