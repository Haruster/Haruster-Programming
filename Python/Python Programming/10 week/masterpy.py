import random

ranNum = random.randrange(1, 101)

print(ranNum)

for i in range(5):

    userNum = int(input('1에서 100사이 수를 추측하라 : '))

    if userNum == ranNum:

        print('정답')
        break

    elif userNum > ranNum:

        print('입력한 수가 큽니다.')

    else:

        print('입력한 수가 작습니다.')

if i == 4 and userNum != ranNum: # i가 4일 때 userNum과 ranNum이 같지 않을 때만 이를 실행하는 걸로 해서 오류를 수정한다. i==4로 되어 있으면 i가 4이면 그냥 실행이 되기 때문에 추가로 조건을 걸어준다.
    print('임의의 수는 ', ranNum)
    print('너짐')

'''

'''