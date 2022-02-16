# for문을 이용해서 1 ~ 100까지의 정수 중에서 3과 7의 공배수와 최소공배수 출력

min = 1

for num in range(1, 101, 1): # 1부터 100까지 1씩 증가

    if num % 3 == 0 and num % 7 == 0:
        
        print('공배수 %d' %num)

        if min == 1:

            min = num

print('최소공배수 %d' %min)