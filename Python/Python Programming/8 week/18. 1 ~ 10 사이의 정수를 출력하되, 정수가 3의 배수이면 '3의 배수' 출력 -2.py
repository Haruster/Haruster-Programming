# 1 ~ 10 사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수' 출력

for num in range(1, 11, 1): # 1부터 10까지 1씩 증가

    print('num = %d' %num)

    if num % 3 == 0:

        print('3의 배수!')