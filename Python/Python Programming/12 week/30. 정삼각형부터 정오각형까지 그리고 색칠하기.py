# 정삼각형부터 정오각형까지 그리고 색칠하기

import turtle

t = turtle.Turtle()
t.shape('turtle')

# x, y 좌표 및 회전각도 데이터

datas = [(0, 0, 'red', 120, 120, 120), (100, 0, 'green', 90, 90, 90, 90), (200, 0, 'blue', 72, 72, 72, 72, 72)]

for points in datas:

    t.up()
    t.goto(points[0], points[1]) # x, y 좌표 설정
    t.down()
    t.fillcolor(points[2]) # 색상 설정
    t.begin_fill() # 채색 시작

    for num in range(2, len(points)): # 회전하면서 그리기

        t.forward(50)
        t.left(points[num])

t.end_fill() # 채색 끝

