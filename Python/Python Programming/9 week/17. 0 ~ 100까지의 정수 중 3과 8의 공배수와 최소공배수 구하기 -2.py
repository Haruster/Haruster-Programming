# 0 ~ 100까지의 정수 중 3과 8의 공배수와 최소공배수 구하기 -2.py

num = 1
min = 1

while num <= 100:

    if num % 3 == 0 and num % 8 == 0:

        print('공배수 : %d' %num)

        if min == 1:

            min = num

    num += 1

print('최소공배수 %d' %min)