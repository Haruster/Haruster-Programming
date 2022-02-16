# 1 ~ 30까지의 정수 중 홀수와 짝수를 구분하여 출력

num = 1

while num <= 30:

    if num % 2 == 0:

        print('짝수 : %d' %num)

    else:

        print('홀수 : %d' %num)

    num += 1