# 생존율 출력 프로그램

lifetime = int(input('최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요 : '))

if lifetime <= 60:

    print('생존율 : 85%')

elif lifetime <= 120:

    print('생존율 : 76%')

elif lifetime <= 180:

    print("생존율 : 66%")

elif lifetime <= 240:

    print('생존율 : 57%')

elif lifetime <= 300:

    print('생존율 : 47%')

elif lifetime <= 360:

    print('생존율 : 37%')

else:

    print('생존율 : 25% 미만')