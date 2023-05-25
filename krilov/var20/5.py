def f(n):
    b = bin(n)[2:]
    if int(b,2) % 4 == 0:
        b = b + "00"
    elif int(b, 2) % 4 == 1:
        b = b + "01"
    elif int(b, 2) % 4 == 2:
        b = b + "10"
    elif int(b, 2) % 4 == 3:
        b = b + "11"
    return int(b,2)

for i in range(1,100):
    print(i,"--",f(i))

