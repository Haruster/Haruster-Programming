# 도형 채색하기

import turtle

t = turtle.Turtle()

t.shape("turtle")

t.fillcolor('blue') # 색상 ('blue')을 설정한다.
t.begin_fill() # 채색시작
t.circle(50) # 반지름이 50인 원을 그린다.
t.end_fill() # 채색 끝

t.up()
t.goto(90, 0)
t.down()

t.fillcolor('black') # 색상 ('black')을 설정한다.
t.begin_fill() # 채색시작
t.circle(50) # 반지름이 50인 원을 그린다.
t.end_fill() # 채색 끝

t.up()
t.goto(180, 0)
t.down()

t.fillcolor('red') # 색상 ('red')을 설정한다.
t.begin_fill() # 채색시작
t.circle(50) # 반지름이 50인 원을 그린다.
t.end_fill() # 채색 끝

t.up()
t.goto(45, -50)
t.down()

t.fillcolor('yellow') # 색상 ('yellow')을 설정한다.
t.begin_fill() # 채색시작
t.circle(50) # 반지름이 50인 원을 그린다.
t.end_fill() # 채색 끝

t.up()
t.goto(135, -50)
t.down()

t.fillcolor('green') # 색상 ('green')을 설정한다.
t.begin_fill() # 채색시작
t.circle(50) # 반지름이 50인 원을 그린다.
t.end_fill() # 채색 끝



