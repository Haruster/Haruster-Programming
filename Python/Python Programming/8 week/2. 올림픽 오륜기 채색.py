# 올림픽 오륜기 채색

import turtle

t = turtle.Turtle()

t.shape('turtle')

t.speed(10)

t.fillcolor('blue') # 색상을 blue로 설정한다.
t.begin_fill() # 채색 시작
t.circle(50) # 반지름이 50인 원 그리기
t.end_fill() # 채색 종료

t.up() # 그리기 종료

t.goto(80, 0) # 좌표를 (80, 0)으로 이동한다.
t.down() # 그리기 시작
t.fillcolor('black') # 색상을 'black'으로 설정한다.
t.circle(50) # 반지름이 50인 원 그리기
t.end_fill() # 채색 종료
t.up() # 그리기 종료

t.goto(160, 0) # 좌표를 (160, 0)으로 이동한다.
t.down() # 그리기 시작
t.fillcolor('red') # 색상을 'red'로 설정한다.
t.circle(50) # 반지름이 50인 원을 그린다.
t.end_fill() # 채색 종료
t.up() # 그리기 종료

t.goto(40, -70) # 좌표를 (40, -70)으로 이동한다.
t.down() # 그리기 시작
t.begin_fill('yellow') # 색상을 'yellow'로 이동한다
t.circle(50) # 반지름이 50인 원을 그린다.
t.end_fill() # 채색 종료
t.up() # 그리기 종료

t.goto(120, -70) # 좌표를 (120, -70)으로 이동한다.
t.down() # 그리기 시작
t.begin_fill('green') # 색상을 'green'으로 설정한다.
t.circle(50) # 반지름이 50인 원을 그린다.
t.up() # 그리기 종료
