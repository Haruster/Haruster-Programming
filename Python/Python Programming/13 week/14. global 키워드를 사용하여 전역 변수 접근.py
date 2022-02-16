# global 키워드를 사용하여 전역 변수 접근

    # global 키워드 : '전역을 가리킨다'는 의미로 global 키워드를 사용하여 전역 변수에 접근할 수 있다.

num = 10 # 전역 변수 num 선언

def fun1(): # 함수 정의

    global num # 전역 변수 num 설정
    
    num = 20 # 전역 변수 num 변경

    print('num : ', num) # 전역 변수 num 사용

print('num : ', num) # 전역 변수 num 사용

fun1() # 함수 호출

print('num : ', num) # 전역 변수 num 사용