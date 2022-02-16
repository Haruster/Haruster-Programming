# 속도 위반 경고하기
# 제한 속도가 50km/h인 도로에서 속도위반을 하는 자동차에 경고를 하는 프로그램 작성

carSpeed = int(input('자동차의 현재 속도는 : '))

if carSpeed >= 50:
    print('속도 위반 !!!')