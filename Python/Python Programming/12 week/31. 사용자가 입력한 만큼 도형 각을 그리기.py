# 사용자가 입력한 만큼 도형 각을 그리기

import turtle 

t = turtle.Turtle()
t.shape('turtle')

userInput = int(input('몇 각형을 그리겠습니까? : '))

for i in range(userInput):

    t.forward(5)

    start = 180 - ((180 * (n - 2)) / n)
    
    t.left(start)