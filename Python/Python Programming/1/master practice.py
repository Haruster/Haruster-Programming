'''
# 변수에 숫자를 저장할 때는 단순하게 숫자만 입력한다. 
MyNumber = 10

print(myNumber) # 10이 출력됨

myNumber = 3.14

print(myNumber) # 3.14가 출력됨


# 실수형 : 소수점이 있는 숫자 데이터를 의미한다.
    # 따라서 정수형을 의도했더라도 3.0을 입력하면 실수형으로 인식하며 실수형은 메모리의 크기에 제약을 받기 때문애 
        # 소수점 16번째 자리까지만 메모리에 저장하고 나머지는 손실한다.

MyNum1 = 3.12

print(MyNum1)

MyNum2 = 3.123456789012345678901234567890

print(MyNum2)


# 정수형 : 소수점이 없는 숫자 데이터 
myNum1 = 123

print(myNum1)

myNum2 = 12345678901234567890123456789012345678901234567890;

print(myNum2)


# 숫자와 문자의 구분 

var1 = 777
var2 = '777'

print(var1)

print(var2)

# var1 : 점수 777이 저장됨
# var2 : 문자열 '777'이 저장됨


# 논리형
# 참과 거짓을 나타내는 논리 데이터인 True와 False가 있다.
# True와 False도 데이터이므로 변수에 저장할 수 있다. 

flag = True

print(flag)

flag = False

print(flag)


# 자료형 조회 
# type() 함수 : 변수에 저징된 데이터가 어떤 자료형인지 알기 위해 사용하는 함수이다. 
type(123) # 정수형
type('123') # 문자형

myVar = 3.14

type(myVar) # 실수형

myvar = True 

type(myvar) # 논리형


# 자료형 변환
# 문자 '123'을 실수로 변환

myVar = '123'
type(myVar)

myVar = float(myVar)

type(myVar)


# 자료형 변환
# 문자 '123'을 정수로 변환

myVar = '123'
type(myVar)

myVar = int(myVar)
type(myVar)



# 자료형 변환
# 문자형을 논리형으로 변환하기 
# - 빈 문자("")를 논리형으로 바꾸면 False로 변환되고, 그 외 나머지 문자는 모두 True로 변환됨.
# 공백 문자('')도 True로 변환됨

myVar = ''
type(myVar)

myVar = bool(myVar)

type(myVar)

print(myVar)


# 자료형 변환
# 문자형을 논리형으로 변환하기 
# - 빈 문자("")를 논리형으로 바꾸면 False로 변환되고, 그 외 나머지 문자는 모두 True로 변환됨.
# 공백 문자('')도 True로 변환됨

myVar = 'Hello'
type(myVar)

myVar = bool(myVar)

type(myVar)

print(myVar)


# 자료형 변환
# 정수형 10을 문자로 변환

myVar = 10

type(myVar)

myVar = str(myVar)

type(myVar)


# Hello C C++!을 5번 출력
# 변수를 사용하지 않고 print()함수를 5번 사용

print('Hello C C++!')
print('Hello C C++!')
print('Hello C C++!')
print('Hello C C++!')
print('Hello C C++!')



# Hello Python!을 5번 출력
# 변수를 사용하지 않고 print()함수를 5번 사용

print('Hello Python!')
print('Hello Python!')
print('Hello Python!')
print('Hello Python!')
print('Hello Python!')


#변수를 사용해서 Hello Python! 출력
introstr = 'Hello C C++!'

print(introstr)
print(introstr)
print(introstr)
print(introstr)
print(introstr)


#변수를 사용해서 Hello Python! 출력
introstr = 'Hello Python!'

print(introstr)
print(introstr)
print(introstr)
print(introstr)
print(introstr)


# 온도 설정 프로그램

currentTemp = 25 # 현재 온도
targetTemp = 30 # 설정 온도

print('현재 온도')

print(currentTemp)

print('설정 온도')

print(targetTemp)

print('설정 온도와 현재 온도의 차이')

print(targetTemp - currentTemp)


# 데이터 복사
# 할당 연산자(=)를 이용하면 변수에 저장된 데이터를 다른 변수에 쉽게 복사할 수 있다.

var1 = 123
var2 = var1

print(var1)
print(var2)


# 데이터 변경
# var1과 var2는 전혀 다른 방이며 서로 영향을 끼치지 않는다.
# var2에 var1의 데이터를 복사한 후 var1의 데이터를 변경하면 var1은 변경되지만 var2는 변경되지 않는 것을 확인할 수 있다.
var1 = 123
var2 = var1

var1 = 321

print(var1)

print(var2)


# 데이터 복사 & 변경
# var1 변수에 문자, 문자열, 정수, 실수를 차례로 변경하고 출력

var1 = 'H' # 문자

print(var1)

var1 = 'Hello Python!' # 문자열

print(var1)

var1 = 10 # 정수

print(var1)

var1 = 3.14 # 실수

print(var1)

var1 = True # 논리형

print(var1)


# input 문제

userName = ''
userAge = ''
userName = input('이름을 입력하세요 : ')

print('사용자 이름')

print(userName)

userAge = input('나이를 입력하세요 : ')

print('사용자 나이')

print(userAge)


# input() 함수
# 사용자에게 데이터를 입력 받을 때 사용하는 함수이다.
# input() 함수로 사용자에게 입력 받은 데이터를 usrData 변수에 저장

usrData = input() 

print(usrData)


#input()함수
# print() 함수 대신 input() 함수의 매개변수 이용

userData = input('데이터를 입력하세요 : ')

print(userData)


# print() 함수를 이용하여 데이터 입력을 유도

print('데이터를 입력하세요 : ')

userData = input()

print(userData)


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


'''