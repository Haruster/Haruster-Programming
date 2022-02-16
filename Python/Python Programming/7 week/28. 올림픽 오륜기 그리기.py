# 올림픽 오륜기 그리기

import turtle

t = turtle.Turtle()

t.shape('turtle')

t.speed(8)

t.circle(50) # 반지름이 50인 원을 그린다.

t.up() # 그리기를 중단한다.
t.goto(90, 0) # 좌표를 (90, 0)으로 이동한다.
t.down() # 그리기를 시작한다.

t.circle(50) # 반지름이 50인 원을 그린다.

t.up() # 그리기를 중단한다.
t.goto(180, 0) # 좌표를 (180, 0)으로 이동한다.
t.down()

t.circle(50)

t.up() # 그리기를 중단한다.
t.goto(45, -50) # 좌표를 (45, -50)으로 이동한다.
t.down()

t.circle(50)

t.up()
t.goto(135, -50) # 좌표를 (135, -50)으로 이동한다.
t.down()

t.circle(50)

