# 사용자 정의 육각형

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
t.left(angle)
t.forward(length)


