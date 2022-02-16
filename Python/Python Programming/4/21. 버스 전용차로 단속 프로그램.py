# 버스 전용차로 단속 프로그램

print('1. 월~금, 2. 토요일, 3. 공휴일')

dayweek = int(input('요일을 선택하세요. : '))

if dayweek == 1:

    print('버스 전용차로 단속 중입니다.')
    print('1. 버스, 2. 승용차')

    carType = int(input('차종을 입력하세요. : '))

    if carType != 1:

        print('버스 전용차로 위반!!')

    else:

        print('버스입니다.')

else: 

    print('토요일 및 공휴일은 단속하지 않습니다.')