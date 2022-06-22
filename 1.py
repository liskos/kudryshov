norm_x = (0, 1000)
x = int(input())
if x // 1 <= 9:
        print ('однозначное')
elif x // 10 <= 9:
        print ('двузначное')
elif x // 100 <= 9:
        print ('трехзначное')
