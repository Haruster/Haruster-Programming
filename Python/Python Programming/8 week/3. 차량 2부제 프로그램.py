# 차량 2부제 프로그램

from datetime import datetime # 날짜 모듈 불러오기

dayNum = datetime.today().day # 현재 일(날짜) 구하기
carNum = int(input('차량 번호 4자리를 입력하세요 : ')) # 차량 번호 입력하기

print('오늘 날짜 : ', dayNum, '일')

if dayNum % 2 == 0:

    print('오늘 입차 : 번호가 짝수인 차량')

else: 

    print('오늘 입차 : 번호가 홀수인 차량')

if dayNum % 2 == carNum % 2:

    print('귀하의 차량은 입차 가능합니다.')

else:

    print('귀하의 차량은 입차 불가합니다.')
