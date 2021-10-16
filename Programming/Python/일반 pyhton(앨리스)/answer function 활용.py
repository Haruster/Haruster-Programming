def plus_print(a, b): # 매개변수 a와 b를 가진 함수 plus_print를 선언한다.

    print(a + b) #a와 b를 더해준다

def times_return(a, b): # 매개변수 a와 b를 가진 함수 times_return을 선언한다.

    return a * b # a와 b를 반환해준다.
    
plus_print(3, 4) #이미 함수내에서 print를 하고 있으므로 a와 b의 값만 넣어주면 된다.
print(times_return(3, 4)) #함수의 반환값이 a * b이므로 print문을 넣어서 a와 b를 곱한 값을 출력하게 된다.