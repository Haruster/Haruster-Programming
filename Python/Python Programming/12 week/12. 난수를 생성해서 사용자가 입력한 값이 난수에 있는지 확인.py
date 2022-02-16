# 난수를 생성해서 사용하자 입력한 값이 난수에 있는지 확인

import random 

a = (random.sample(range(1, 1000), 100)) # 1부터 1000까지 100가지의 난수를 생성

inputData = input('사용자 값을 입력해주세요 : ')

print(inputData in a) # 확인하기

print('생성된 난수는 다음과 같습니다. -> ', a)


