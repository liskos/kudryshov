import sys
sys.stdin("F:\яндекс\YandexDisk\Информатика\ЕГЭ информатика\2022 2023\открытый вариант фипи\ИНФ_Доп.файлы\1\1_17.txt")

n = int(input())
a = [int(input()) for _ in range(n)]
m = max([x for x in a if len(str(x))==2])
k = []
for i in range(n-1):
    s1 = len(a[i])
    s2 = len(a[i+1])
    if ((s1 == 2) or (s2 == 2)) and (s1 != s2) and ((a[i]+a[i+1])% m == 0):
        k.append(a[i]+a[i+1])
print(len(k), max(k))
