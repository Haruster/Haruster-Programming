# 변수를 활용하여 정삼각형 그리기
# 정삼각형의 내각은 항상 120도로 일정함

import turtle

t = turtle.Turtle()

t.shape('turtle')

angle = 120 # 120을 angle 변수에 저장한다.

t.right(angle) # 오른쪽으로 angle만큼 회전한다.
t.forward(100)
t.left(angle) # 왼쪽으로 angle만큼 회전한다.
t.forward(100)
t.left(angle) # 왼쪽으로 angle만큼 회전한다.
t.forward(100)