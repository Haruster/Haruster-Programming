# 냉방 기능 프로그램 while문 이용 -2

cT = 30.0
tT = float(input('희망 온도 : '))

while tT < cT:

    cT -= 0.1

    print('햔제 온도 %5.2f' %cT)
    print('현재 온도 ', format(cT, '.2f'))

print('에어컨 끔')