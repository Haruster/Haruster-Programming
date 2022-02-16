# 냉방 기능 프로그램 while문 이용

currentTemperature = 30.0
targetTemperature = float(input('희망 온도를 입력하세요 : '))

while targetTemperature < currentTemperature:

    currentTemperature -= 0.1

    print('현재 온도 : ', format(currentTemperature, '.2f'))

print('냉방 기능 종료 !!')