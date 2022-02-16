# 컴퓨터가 임의로 생성한 난수가 홀수인지 짝수인지 판별

# 컴퓨터가 임의로 생성한 난수가 홀수인지 짝수인지 맞추는 게임

import random

randNum = random.randint(1, 100)

print('홀짝 맞추기 게임')

userNum = int(input('홀수이면 1, 짝수이면 2번을 눌러주세요 : '))

print('생성된 난수는 ', randNum, '입니다.')

if randNum % 2 == userNum % 2:

    print('정답')

else:

    print('오답')


