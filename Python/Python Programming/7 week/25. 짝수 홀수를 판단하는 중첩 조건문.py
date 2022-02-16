# 짝수 / 홀수를 판단하는 중첩 조건문

num = int(input('양의 정수를 입력하세요. : '))

if num > 0: # num이 양수라면

    print('num : ', num)

    if num % 2 == 0: # num을 2로 나눈 나머지가 0이라면

        print('num은 짝수')

    else: # num을 2로 나눈 나머지가 0이 아니라면

        print('num은 홀수')

else:

    print('num은 양수가 아니다.')