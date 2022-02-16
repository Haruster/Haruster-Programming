# 정삼각형부터 정육각형까지 그리기

import turtle

t = turtle.Turtle()
t.shape('turtle')

# x, y 좌표 및 회전각도 데이터

datas = [(0, 0, 120, 120, 120), (100, 0, 90, 90, 90, 90), (200, 0, 72, 72, 72, 72, 72), (300, 0, 60, 60, 60, 60, 60, 60)]

for points in datas:

    t.up()
    t.goto(points[0], points[1]) # x, y 좌표 설정
    t.down()

    for num in range(2, len(points)): # 회전하면서 그리기

        t.forward(50)
        t.left(points[num])

