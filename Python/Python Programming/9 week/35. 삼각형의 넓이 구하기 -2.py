# 삼각형의 넓이 구하기 -2

count = 1
maxArea = 150

while True:

    result = ((count * 2) * (count * 3)) / 2

    if result > maxArea:

        break

    print('삼각형 넓이 : %d' %result)

    count += 1