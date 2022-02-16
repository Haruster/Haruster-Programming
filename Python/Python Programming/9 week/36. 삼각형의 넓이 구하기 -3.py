# 삼각형의 넓이 구하기 -3.py

count = 1
maxArea = 150

while True:

    result = ((count * 2) * (count * 3)) / 2

    print('삼각형 넓이 : %d' %result)

    if result > maxArea:

        break

    count += 1