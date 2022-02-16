# 컴퓨터와 난수를 이용한 가위바위보 게임
while True:
    import random

    ranNum = random.randint(1, 3)

    print('가위바위보 게임')

    userNum = int(input('가위 1, 바위 2, 보 3 :'))

    print('컴퓨터가 만든 수', ranNum)

    if (userNum == 1 and ranNum == 3) or (userNum == 2 and ranNum == 1) or (userNum == 3 and ranNum == 2):

        print('너 이김')

    elif (userNum == 1 and ranNum == 2) or (userNum == 2 and ranNum == 3) or (userNum == 3 and ranNum == 1):

        print('너 짐')

    elif userNum == ranNum:

        print('비김')