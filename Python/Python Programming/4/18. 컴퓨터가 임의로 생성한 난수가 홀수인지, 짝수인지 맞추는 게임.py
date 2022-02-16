# 컴퓨터가 임의로 생성한 난수가 홀수인지 짝수인지 맞추는 게임

while True:

    import random

    ranNum = random.randint(1, 100)


    print('홀짝게임')

    userNum = int(input('홀수면 1, 짝수면 2를 누르세요 : '))

    print('컴퓨터로 만든 수 ', ranNum)

    if ranNum % 2 == userNum % 2:
    print('정답')

    else: