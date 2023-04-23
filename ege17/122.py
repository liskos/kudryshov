def f(n):
    return ((n % 16 == 0) or (n % 48 == 0)) and ((n % 2 == 0) or (n % 3 != 0) or (n % 18 != 0) or (n % 63 != 0))


a = [i for i in range(1110,1111101 + 1) if f(i)]
print(len(a),min(a))


