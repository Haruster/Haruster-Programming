# 사용자의 선택에 따라 게임의 종료와 진행을 결정하는 프로그램

flag = True

while flag:

    inputData = int(input('1 : 진행, 2. 종료'))

    if inputData == 1:
        flag = True
        print('게임 진행')

    else:
        flag = False
        print('게임 종료')