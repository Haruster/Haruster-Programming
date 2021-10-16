# 사용자에게 회전 각도와 전진길이를 입력 받아 정오각형 그리기
# 회전하는 각도의 변수 : angle / 전진하는 길이의 변수 : length
# 정오각형의 내각은 72도로 일정함

import turtle

t = turtle.Turtle()
t.shape('turtle')
angle = int(input('회전 각도를 입력하세요 : '))
length = int(input('전진 길이를 입력하세요 : '))
t.forward(length)
t.left(angle)
t.forward(length)
t.left(angle)
t.forward(length)
t.left(angle)
t.forward(length)
t.left(angle)
t.forward(length)

