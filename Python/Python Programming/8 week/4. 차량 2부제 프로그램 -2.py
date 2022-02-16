# 차량 2부제 프로그램 -2

from datetime import date, datetime # 날짜 모듈 불러오기

dayNum = datetime.today().day # 현재 일(날짜)구하기
carNum = int(input('차량 번호 4자리를 입력해주세요 : ')) # 차량 번호 입력하기

print('오늘 날짜는 %d일 입니다' %dayNum)

if dayNum % 2 == 0:

    print('오늘 짝수 가능')

else:

    print('오늘 홀수 가능')

if dayNum % 2 == carNum % 2:

    print('입차 가능')

else:

    print('입차 불가능')