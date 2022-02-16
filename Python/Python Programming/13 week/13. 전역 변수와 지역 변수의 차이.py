# 전역 변수와 지역 변수의 차이

num = 10 # 전역 변수 num 선언

def fun1(): # 함수 정의

    num = 20 # 지역 변수 num 선언
    print('num : ', num) # 지역 변수 num 사용(함수 안에서 num을 먼저 찾는다.)

print('num : ', num) # 전역 변수 num 사용
fun1() # 함수 호출