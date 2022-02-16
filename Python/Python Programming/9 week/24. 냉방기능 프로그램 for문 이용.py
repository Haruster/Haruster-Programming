# 냉방기능 프로그램 for문 이용

currentTemperature = 30.0
targetTemperature = float(input('희망 온도를 입력해주세요 : '))

for i in range(1000): # 반복 횟수를 정확히 설정할 수 없다.

    currentTemperature -= 0.1

    print('현재 온도 : ', format(currentTemperature, '.2f'))

    if currentTemperature <= targetTemperature:

        break

print('냉방 기능 종료!!')