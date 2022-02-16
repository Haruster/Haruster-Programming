# 1 ~ 10까지 정수를 더하되 결과가 30이상이 될 때 정수를 찾기(break 키워드 사용)

num = 1
sum = 0

while num < 11:

    sum += num

    if sum >= 30:

        print('num : ', num)

        break

    num += 1

