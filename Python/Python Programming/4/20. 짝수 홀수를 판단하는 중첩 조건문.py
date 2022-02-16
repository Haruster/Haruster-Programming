# 짝수 홀수를 판단하는 중첩 조건문

'''
중첩 조건문 : 조건문 내에 또 다른 조건문을 사용한 조건문
- 바깥에 있는 조건문 1의 결과가 True인 경우 조건문 2를 실행함
- 만약 조건문 1의 결과가 False이면 조건문 2는 실행하지 않고 else문을 실행한다.
'''

num = int(input('양의 정수를 입력하세요 : '))

if num > 0: # num이 양수라면

    print('num : ', num)

    if num % 2 == 0: # num을 2로 나눈 나머지가 0이라면

        print('num은 짝수')

    else: # num을 2로 나눈 나머지가 0이 아니라면

        print('num은 홀수')

else:

    print('num은 양수가 아니다.')