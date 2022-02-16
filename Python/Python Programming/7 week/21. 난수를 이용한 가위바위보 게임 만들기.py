# 난수를 이용한 가위바위보 게임 만들기.py

import random

randNum = random.randint(1, 3)

print('가위바위보 게임')

userNum = int(input('가위면 1, 바위면 2, 보면 3을 입력해주세요 : '))

print('컴퓨터가 만든 수', randNum)

if (userNum == 1 and randNum == 3) or (userNum == 2 and randNum == 1) or (userNum == 3 and randNum == 2):

    print('너 이김')

elif (userNum == 1 and randNum == 2) or (userNum == 2 and randNum == 3) or (userNum == 3 and randNum == 1):

    print('너 짐')

elif userNum == randNum:

    print('비김')

