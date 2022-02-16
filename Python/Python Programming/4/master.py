'''
# if문의 기본 예제
# if문의 조건식 결과가 참이면 다음 줄을 실행하고 거짓이면 아무것도 하지 않는다.

#if문 : 조건문의 기본적인 구문으로 사용 빈도가 가장 높다.
    # if 키워드 : 조건문을 선언하기 위한 키워드
    # 조건식 : 특정 조건을 기술하며 조건식의 결과에 따라 실행문의 실행여부가 결정된다.
    # 콜론 : 코드 블록의 시작을 나타내는 것으로 콜론 이후부터가 실행될 문장이다.
    # 실행문 : 조건문의 결과가 참일 경우 실행되는 명령문으로 조건식이 거짓이면 실행되지 않는다.

num = int(input('숫자를 입력하세요 . : '))

if num > 10: # 조건문
    print('num은 10보다 크다.') # 실행문


# 속도 위반 경고하기
# 제한 속도가 50km/h인 도로에서 속도위반을 하는 자동차에 경고를 하는 프로그램 작성

carSpeed = int(input('자동차의 현재 속도는 : '))

if carSpeed >= 50:
    print('속도 위반 !!!')


# 어린이의 신장을 입력하면 놀이기구의 탐승 여부가 출력되는 프로그램(놀이기구의 탑승은 신장 120cm~160cm까지 가능함)

height = int(input("키 입력 : "))

if height >= 120 and height <= 160:

    print("탑승가능")


# 코드 블록의 마지막 
# - 들여쓰기를 하지 않으면 코드 블록이 종료되었다고 간주한다.

#코드 블록 들여쓰기 -1
num = int(input('숫자를 입력하세요 : '))

if num > 10:

    print('num은 10보다 크다')

print('num : ', num)


# 코드 블록의 마지막 
#- 들여쓰기를 하지 않으면 코드 블록이 종료되었다고 간주한다.

# 코드 블록 들여쓰기 -2

num = int(input('숫자를 입력하세요 : '))

if num > 10:

print('num은 10보다 크다')
print('num : ', num)

# 들여쓰기를 하지 않았기 때문에 오류가 발생한다.


코드 블록 : 코드의 시작과 끝을 나타내는 역할을 한다.

    if num > 10:
        print("num은 10보다 크다")
        print('num : ', num)

- 코드 블록 내 모든 행은 반드시 들여쓰기를 해야한다.
- 들여쓰기를 하지 않으면 에러가 발생한다.

# 코드 블록의 띄어쓰기
- 보통 tap키를 써서 4칸씩 공백을 둔다.
- 꼭 4칸을 지킬 필요는 없으며, 공백의 개수가 달라도 정상적으로 실행된다.

# 코드 블록의 들여쓰기의 주의사항
- 공백 개수가 자유롭다고 해도 코드 블록 내에서의 공백은 들쭉날쭉하면 안되며 모든 행의 공백 개수는 동일해야 한다.

# 코드 블록의 마지막 
- 들여쓰기를 하지 않으면 코드 블록이 종료되었다고 간주한다.

# 한줄 코드 블록
- 코드 블록이 한 줄인 경우 콜론 뒤애 허너 쥴 코드 블록을 붙여 코드를 간략하게 할 수 있다.

    if number > 0: print("양수")


# 점수가 80점 이상이면 함격입니다.를 출력하고 80점 미만이면 아쉽습니다. 다시 도전해주세요를 출력하는 프로그램 if문

score = int(input('점수를 입력하세요 : '))

if score >= 80:
    print("합격입니다.")

# 80점 미만인 도전자에게는 if문으로 메세지를 전달하지 못한다.


# 점수가 80점 이상이면 함격입니다.를 출력하고 80점 미만이면 아쉽습니다. 다시 도전해주세요를 출력하는 프로그램 if문 두개 사용

score = int(input('점수를 입력하세요 : '))

if score >= 80:
    print('합격입니다.')

if score < 80:

    print('아쉽습니다. 다시 도전해주세요')

# 시나리오는 충족하지만 if~else문을 사용하면 if문의 중복을 보완할 수 있다.


if~else문 : 양자택일을 해야할 때 사용한다.

if score >= 80:

    print("함격입니다.")

else:
    print("아쉽습니다. 다시 도전해주세요 ")



# 점수가 80점 이상이면 함격입니다.를 출력하고 80점 미만이면 아쉽습니다. 다시 도전해주세요를 출력하는 프로그램 if~else문 사용

score = int(input('점수를 입력하세요.'))

if score >= 80:

    print('합격입니다.')

else:

    print('아쉽습니다. 다시 도전해주세요.')



pass키워드 : 프로그램에서 조건문을 코딩할 때 실행문이 아직 정해지지 않은 경우에 사용한다.

- 필요한 문장이 없는 경우 프로그램을 다음 단계로 넘기는 역할을 한다.

# pass 키워드를 사용하지 않아 에러가 발생하는 경우

score = int(input('점수를 입력하세요. : '))

if score >= 80:

    # 80 이상인 경우 실행문

else:

    # 80미만인 경우 실행문



# pass 키워드를 사용하여 에러 발생 방지

score = int(input('점수를 입력하세요 : '))

if score >= 80:

    pass # 80이상인 경우 실행문

else:

    pass # 80미만인 경우 실행문


# 자동 온도 조절 장치 

temp = int(input('기계 온도를 입력하세요 : '))

if temp >= 40:

    print('팬(Fan) 가동')

else: 

    print('팬(Fan) 중지')



# 사용자가 입력한 양의 정수를 3으로 나눈 후 소수점 첫 자리에서 반올림

number = int(input('양의 정수 입력 : '))# 사용자가 양의 정수 입력

result = number / 3

if (result - int(result)) >= 0.5:

    result = int(result) + 1

else:

    result = int(result)


print('결과 : ', result)



if~elif문 : 다중 비교를 할 때 사용하는 조건문
- elif는 else if의 줄임말이다.


# 요구사항에 맞는 프로그램 작성

# 점수가 90점 이상이면 A출력
# 점수가 80점 이상 90점 미만이면 B 출력
# 점수가 70점 이상 80점 미만이면 C 출력
# 점수가 60점 이상 70점 미만이면 D 출력
# 점수가 60점 미만이면 F 출력

score = int(input('점수를 입력하세요. : '))

if score >= 90: # 점수가 90점 이상이면 'A'출력
    print('A')

elif score >= 80: # 점수가 90점 미만 80점 이상이면 'B' 출력
    print('B')

elif score >= 70: # 점수가 80점 미만 70점 이상이면 'C' 출력
    print('C')

elif score >= 60: # 점수가 70점 미만 60점 이상이면 'D' 출력
    print('D')

else: # 점수가 60점 미만이면 'F'를 출력
    print('F')



요구 사항에 맞는 프로그램 만들기
- if-elif문을 이용해서 다중 비교를 하더라도 실제로 실행되는 실행문은 하나뿐이거나 아예 없을 수 있다.
-> 따라서 적절한 조건식의 순서 설계가 필요하다.

- 조건식에 비교연산과 논리연산을 같이 사용해서 범위를 한정 짓는 방법
- 조건식의 순서와 상관없이 원하는 프로그램을 구현할 수 있고 조건식이 명시적으로 기술되어 코드를 이해하는데 도움을 준다.
- 단, 코드가 조금 늘어날 수 있다.


# 요구 사항에 맞는 프로그램 만들기

score = int(input('점수를 입력하세요 : '))

if score >= 60 and score < 70: # 60 이상 70미만이면 'D' 출력
    print('D')

elif score >= 80 and score < 90: # 80 이상 90미만이면 'B' 출력
    print('B')

elif score >= 70 and score < 80: # 70 이상 80미만이면 'C' 출력
    print('C')

elif score >= 90: # 90 이상이면 'A' 출력
    print('A')

else: # 60 미만이면 'F' 출력
    print('F')


요구 사항에 맞는 프로그램 만들기
- if-elif문을 이용해서 다중 비교를 하더라도 실제로 실행되는 실행문은 하나뿐이거나 아예 없을 수 있다.
-> 따라서 적절한 조건식의 순서 설계가 필요하다.

# score가 점수에 상관없이 모두 D를 출력

score = int(input('점수를 입력하세요 : '))

if score >= 60: # 60점 이상이면 'D' 출력
    print('D')

elif score >= 80:
    print('B')

elif score >= 70:
    print('C')

elif score >= 90:
    print('A')

else:
    print('F')



# 자동 주문 시스템 만들기

print('Good morning. Nice to meet you.')
print('Where are you from?')
print('Please select a number : ')

choiceNumber = int(input('1. 대한민국 2.USA 3.中国'))

if choiceNumber == 1:
    print('주문하시겠어요?')

elif choiceNumber == 2:
    print('Would you like to order?')

elif choiceNumber == 3:
    print('您要点菜吗？')

else:
    print('Would you like to order?')



# 국가재난지원금 수령액 조회

1인 가구 : 400,000원
2인 가구 : 600,000원
3인 가구 : 800,000원
4인 가구 : 1,000,000원


peopleNumber = int(input('인원수를 입력하세요 : '))

if peopleNumber == 1:
    print('400,000원 지원')

elif peopleNumber == 2:
    print('600,000원 지원')

elif peopleNumber == 3:
    print('800,000원 지원')

elif peopleNumber >= 4:
    print('1,000,000원 지원')



# BMI 프로그램


BMI 지수를 입력한다.
BMI 지수가 90 이하면 '저체중'을 입력한다.
BMI 지수가 90 초과 ~ 110 이하면 '정상체중'을 출력한다.
BMI 지수가 110 초과 ~ 120 이하면 '과체중'을 출력한다.
BMI 지수가 120 초과 ~ 140 이하면 '비만'을 출력한다.
BMI 지수가 140 초과면 '고도비만'을 출력한다.


bmi = int(input('BMI 지수를 입력하세요 : '))

if bmi > 140:
    print('고도 비만')

elif bmi > 120:
    print('비만')

elif bmi > 110:
    print('과체중')
    
elif bmi > 90:
    print('정상 체중')

elif bmi <= 90:
    print('저체중')



# 컴퓨터가 임의로 생성한 난수가 홀수인지 짝수인지 맞추는 게임

while True:

    import random

    ranNum = random.randint(1, 100)


    print('홀짝게임')

    userNum = int(input('홀수면 1, 짝수면 2를 누르세요 : '))

    print('컴퓨터로 만든 수 ', ranNum)

    if ranNum % 2 == userNum % 2:
    print('정답')

    else:




# 컴퓨터와 난수를 이용한 가위바위보 게임
while True:
    import random

    ranNum = random.randint(1, 3)

    print('가위바위보 게임')

    userNum = int(input('가위 1, 바위 2, 보 3 :'))

    print('컴퓨터가 만든 수', ranNum)

    if (userNum == 1 and ranNum == 3) or (userNum == 2 and ranNum == 1) or (userNum == 3 and ranNum == 2):

        print('너 이김')

    elif (userNum == 1 and ranNum == 2) or (userNum == 2 and ranNum == 3) or (userNum == 3 and ranNum == 1):

        print('너 짐')

    elif userNum == ranNum:

        print('비김')




중첩 조건문 : 조건문 내에 또 다른 조건문을 사용한 조건문
- 바깥에 있는 조건문 1의 결과가 True인 경우 조건문 2를 실행함
- 만약 조건문 1의 결과가 False이면 조건문 2는 실행하지 않고 else문을 실행한다.


# 짝수 홀수를 판단하는 중첩 조건문

num = int(input('양의 정수를 입력하세요 : '))

if num > 0: # num이 양수라면

    print('num : ', num)

    if num % 2 == 0: # num을 2로 나눈 나머지가 0이라면

        print('num은 짝수')

    else: # num을 2로 나눈 나머지가 0이 아니라면

        print('num은 홀수')

else:

    print('num은 양수가 아니다.')




# 버스 전용차로 단속 프로그램

print('1. 월~금, 2. 토요일, 3. 공휴일')

dayweek = int(input('요일을 선택하세요. : '))

if dayweek == 1:

    print('버스 전용차로 단속 중입니다.')
    print('1. 버스, 2. 승용차')

    carType = int(input('차종을 입력하세요. : '))

    if carType != 1:

        print('버스 전용차로 위반!!')

    else:

        print('버스입니다.')

else: 

    print('토요일 및 공휴일은 단속하지 않습니다.')




# 출생년도 끝자리와 나이를 입력하면 요구사항에 맞춰 마스크 구매 가능한 요일 출력

endBirthYear = int(input('출생 연도 끝자리를 입력해주세요 : '))

age = int(input('만 나이를 입력해주세요 : '))

if age < 65:

    if endBirthYear == 1 or endBirthYear == 6:

        print('월요일에 구매가능합니다.')

    elif endBirthYear == 2 or endBirthYear == 7:

        print('화요일에 구매가능합니다.')

    elif endBirthYear == 3 or endBirthYear == 8:

        print('수요일에 구매가능합니다.')

    elif endBirthYear == 4 or endBirthYear == 9:

        print('목요일에 구매 가능합니다.')

    elif endBirthyear == 5 or endBirthYear == 0:

        print('금요일에 구매 가능합니다.')

    else:

        print('언제든지 구매 가능합니다.')




# up(), down(), goto() 함수
현재 위치에서 그리기를 잠시 중단하고 다른 좌표로 이동하여 그릴 때 사용한다.

- up() : 도화지에서 붓을 뗀다는 의미로 잠시 그리기를 중단하는 함수이다.

- down() : 반대로 도화지에 붓을 놓고 다시 그림을 그리는 함수이다.

- goto(x, y) : 거북이를 설정한 x좌표, y좌표로 이동하는 함수



# 올림픽 오륜기 그리기(그리기를 중단했다가 다시 그리기)


import turtle 

t = turtle.Turtle()
t.shape('turtle')

t.circle(50) # 반지름이 50인 원을 그린다.

t.up() # 그리기를 중단한다.
t.goto(90, 0) # 좌표를 (90, 0)으로 이동한다.
t.down() # 그리기를 시작한다.

t.circle(50) # 반지름이 50인 원을 그린다.

t.up() # 그리기를 중단한다.
t.goto(180, 0) # 좌표를 (180, 0)으로 이동한다.
t.down() # 그리기를 시작한다.

t.circle(50) # 반지름이 50인 원을 그린다.

t.up() # 그리기를 중단한다.
t.goto(45, -50) # 좌표를 (45, -50)으로 이동한다.
t.down() # 그리기를 시작한다.

t.circle(50) # 반지름이 50인 원을 그린다.

t.up() # 그리기를 중단한다.
t.goto(135, -50) # 좌표를 (135, -50)으로 이동한다.
t.down() # 그리기를 시작한다.

t.circle(50)

'''

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








