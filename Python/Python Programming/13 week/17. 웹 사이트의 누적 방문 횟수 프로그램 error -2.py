# 웹 사이트의 누적 방문 횟수 프로그램 error -2

flag = True
totalVisitor = 0

def countVisitor(): # 함수 정의

    totalVisitor = 0  # 전역 변수 설정
    totalVisitor += 1

while flag:

    inputData = int(input('1. 웹 사이트 방문, 2. 종료'))

    if inputData == 1:

        countVisitor() # 함수 호출

        print('누적 방문 횟수 : ', totalVisitor)

    else:

        flag = False