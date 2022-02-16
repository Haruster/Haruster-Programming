# 중첩 반복문을 이용하여 점찍기
# 1행에서는 한 개, 2행에서는 두 개, 3행에서는 세 개, .... 5행에서는 다섯 개를 출력

for num1 in range(1, 6): # 1에서 5까지 1씩 증가

    for num2 in range(num1): # num만큼 매번 반복

        print('*', end = '')

    print()