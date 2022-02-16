# practice 상단에 위치할 것

Quiz = []

for j in range(3):

    line = []

    print(j + 1, '번째 문제의 문제, 정답, 배점을 입력해주세요 :')

    for i in range(1):
        line.append(input())
        line.append(int(input()))
        line.append(int(input()))

    Quiz.append(line)

Quiz = tuple(Quiz)  # 리스트를 튜플로 데이터 타입 변환

print('문제 : ', Quiz)

answerCount = 0
wrongAnswerCount = 0
totalScore = 0

for item in Quiz:

    print('문제 : ', item[0])

    answer = int(input('정답을 입력하세요 : '))

    if answer == item[1]:

        answerCount += 1

        totalScore += item[2]

    else:

        wrongAnswerCount += 1

print('-' * 30)
print('정답 개수\t : ', answerCount)
print('오답 개수\t : ', wrongAnswerCount)
print('Total Score\t : ', totalScore)
print('-' * 30)

print(type(Quiz))  # 타입 출력

'''
# 튜플 선언

# 튜플(tuple) : 리스트와 비슷하게 데이터를 묶어서 처리하는 컨테이너 자료형이다.
# 튜플에 포함된 아이템은 수정할 수 없다.

fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나') # 튜플 fruits 선언

print(fruits) # 튜플 fruits 출력

print(type(fruits)) # fruits의 데이터 타입 출력


# 튜플과 리스트를 출력하고 타입 함수를 이용해서 타입 출력

fruits = ('사과', '배', '수박')

fruits2 = ['사과', '배', '수박']

print(type(fruits)) # fruits의 타입 출력

print(type(fruits2)) # fruits2의 타입 출력


# 튜플에서 특정 아이템 조회

fruits = ('사과', '포도', '수박', '배', '자두', '복숭아', '바나나') # 튜플 fruits 출력

print(fruits[3]) # fruits에서 인덱스가 3인 아이템 출력

print(fruits[len(fruits) -1]) # 마지막 인덱스 아이템 출력


# 인덱스가 홀수인 아이템 조회

sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')

for index, item in enumerate(sports):

    if index % 2 == 1:

        print(index, ' : ', item)


# 인덱스가 홀수인 아이템 조회 -2

sports = ('태권도', '야구', '농구', '배구', '양궁')

for idx, item in enumerate(sports):

    if idx % 2 == 1:

        print(idx, ' : ', item)



# 인덱스가 짝수인 아이템 조회

sports = ('태권도', '야구', '농구', '배구', '양궁')

for idx, item in enumerate(sports):

    if idx % 2 == 0:

        print(idx, ' : ', item)



# 튜플 내 특정 아이템의 인덱스 조회

fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')

print(fruits.index('포도')) # '포도'에 해당하는 인덱스 조회

print(fruits.index('바나나')) # '바나나'에 해당하는 인덱스 조회


# 아이템 값으로 인덱스 출력

names = ('박찬호', '이승엽','박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')

inputData = input('검색하려는 이름을 입력하세요. : ')

print('이름 : ', inputData, '인덱스 : ', names.index(inputData))


# 튜플에 해당 아이템이 있는지 확인 : in

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

print('Green' in colors) # 'Green'과 일치하는 아이템이 있는지 확인


# 튜플에 해당 아이템이 없는지 확인 : not in

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

print('Green' not in colors) # 'Green'과 일치하는 아이템이 없는지 확인


# 튜플에 해당 아이템이 있는지 확인 -2.py

color = ('red', 'orange', 'yellow', 'green', 'blue')

print('green' in color)


# 튜플에 해당 아이템이 없는지 확인 -2

color = ('red', 'orange', 'yellow', 'green', 'blue')

print('green' not in color)


# 학점 경고 프로그램 만들기

scores = ('A', 'A+', 'B', 'B-', 'F')

if 'F' in scores:

    print('경고')



# 난수를 생성해서 사용하자 입력한 값이 난수에 있는지 확인

import random 

a = (random.sample(range(1, 1000), 100)) # 1부터 1000까지 100가지의 난수를 생성

inputData = input('사용자 값을 입력해주세요 : ')

print(inputData in a) # 확인하기

print('생성된 난수는 다음과 같습니다. -> ', a)



# + 연산자를 이용해서 튜플 결합하기

# + 연산자 : 서로 다른 튜플을 결합할 때 사용한다.

tuple1 = (1, 2, 3) # tuple1 선언
tuple2 = (10, 20, 30) # tuple2 선언

sumTuple = tuple1 + tuple2 # 튜플 결합

print(sumTuple) # 결합된 튜플 출력


# 튜플 슬라이싱

# 슬라이싱 : 튜플에서 필요한 부분의 아이템만 뽑아내는 것을 뜻하며 사용법은 리스트에서 슬라이싱을 할 때와 같다.

animals = ('호랑이', '사자', '곰', '여우', '늑대') # 튜플 생성

print(animals) # 튜플 출력

print(animals[:3]) # 인덱스 3부터 끝까지 아이템 출력
print(animals[1:4]) # 인덱스 1부터 3(4-1)까지의 아이템 출력
print(animals[len(animals)-2:]) # 뒤에서 2개의 아이템을 슬라이싱


# 딕셔너리 선언

ages = {'박찬호' : 48, '박지성' : 40, '박세리' : 50, '이승엽' : 43} # 딕셔너리 선언

print(ages) # 딕셔너리 ages 출력

print(type(ages)) # ages의 타입 출력


# 다양한 데이터 타입을 이용해서 딕셔너리를 선언

dicContainer = {'이름 : ' : '홍길동', '나이' : 25, '주소' : '서대문구 연회로 2길 62', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

print(dicContainer) # 딕셔너리 출력


# 리스트와 튜플간 변환

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

print('colors의 자료형 : ', type(colors)) # colors의 자료형 출력

colors = list(colors) # 튜플을 리스트로 데이터 타입 변환
print('colors의 자료형 : ', type(colors))

colors = tuple(colors) # 리스트를 튜플로 데이터 타입 변환
print('colors의 자료형 : ', type(colors))


# 튜플의 아이템 정렬 : sorted() 함수 -> 반환되는 데이터는 리스트로 변경된다.

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

print(colors)

print('colors의 자료형 : ', type(colors))

cs = sorted(colors)

print(cs)

print('cs의 자료형 : ', type(cs))


# sort() 함수를 이용해서 리스트 정렬

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

cs = sorted(colors)

cs.sort(reverse = True) # 내림차순
print(cs)

cs.sort(reverse = False) # 오름차순
print(cs)


# 딕셔너리 조회

dicContainer = {'이름' : '홍길동', '나이' : 25, '주소' : '서대문구 연희로', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

print(dicContainer)

print(dicContainer['나이']) # 딕셔너리에서 '나이'에 해당하는 아이템 조회
print(dicContainer['취미']) # 딕셔너리에서 '취미'에 해당하는 아이템 조회


# 딕셔너리에 아이템 삽입

dicContainer = {'이름' : '홍길동', '나이' : 25, '주소' : '서대문구 연희로', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

print(dicContainer)

dicContainer['혈액형'] = 0 

print(dicContainer)


# 딕셔너리에 아이템 수정

dicContainer = {'이름' : '홍길동', '나이' : 25, '주소' : '서대문구 연희로', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

dicContainer['몸무게'] = 90 # '몸무게'에 해당하는 아이템 수정

dicContainer['나이'] = dicContainer['나이'] + 1

print(dicContainer) # 딕셔너리 출력


# 딕셔너리에 아이템 삭제

# >>> dicContainer = {'이름' : '홍길동', '나이' : 25, '주소' : '서대문구 연희로', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

# >>> del dicContainer['뭄무게'] # 몸무게에 해당하는 아이템 삭제

# >>> dicContainer # 딕셔너리 출력


# 딕셔너리의 아이템 개수 조희

dicContainer = {'이름' : '홍길동', '나이' : 25, '주소' : '서대문구 연희로', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

print(len(dicContainer))


# 딕셔너리에서 전체 키와 값을 조회(keys()와 value()함수)이용

dicContainer = {'이름' : '홍길동', '나이' : 25, '주소' : '서대문구 연희로', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

print(dicContainer) # 딕셔너리 출력

print(dicContainer.keys()) # 전체 키 조회
print(dicContainer.values()) # 전체 값 조회


# keys()함수로 조회한 키와 for문을 이용하여 각 키에 해당하는 값을 출력

dicContainer = {'이름' : '홍길동', '나이' : 25, '주소' : '서대문구 연희로', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

print(dicContainer) # 딕셔너리 출력

for key in dicContainer.keys(): # key에 해당하는 값 출력

    print(key, '\t: ', dicContainer[key])



# keys()함수로 조회한 키와 for문을 이용하여 각 키에 해당하는 값을 출력

dicCon = {'이름' : '홍길동', '나이' : 25, '주소' : '서대문구 연희로', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

for i in dicCon.keys(): # key에 해당하는 값 출력

    print(i, '\t: ', dicCon[i])



# 중간고사 성적 관리 프로그램

scores = {'C/C++' : 'A', 'Java' : 'B+', '모바일' : 'A', '보안' : 'A+', '해킹' : 'A+', '시스템' : 'A+'}

print('#시나리오1 ')
print(scores)

print('#시나리오2 ')
print('Java : ', scores['Java'])
print('시스템 : ', score['시스템'])

print('#시나리오3 ')
scores['파이썬'] = 'A'
scores['OS'] = 'A+'
print(scores)


print('#시나리오4 ')
scores['Java'] = 'A'
scores['시스템'] = 'A'
print(scores)

print('#시나리오5 ')

for key in scores.keys():

    print(key, '\t:', scores[key])



# 정삼각형부터 정육각형까지 그리기

import turtle

t = turtle.Turtle()
t.shape('turtle')

# x, y 좌표 및 회전각도 데이터

datas = [(0, 0, 120, 120, 120), (100, 0, 90, 90, 90, 90), (200, 0, 72, 72, 72, 72, 72), (300, 0, 60, 60, 60, 60, 60, 60)]

for points in datas:

    t.up()
    t.goto(points[0], points[1]) # x, y 좌표 설정
    t.down()

    for num in range(2, len(points)): # 회전하면서 그리기

        t.forward(50)
        t.left(points[num])



# 정삼각형부터 정오각형까지 그리고 색칠하기

import turtle

t = turtle.Turtle()
t.shape('turtle')

# x, y 좌표 및 회전각도 데이터

datas = [(0, 0, 'red', 120, 120, 120), (100, 0, 'green', 90, 90, 90, 90), (200, 0, 'blue', 72, 72, 72, 72, 72)]

for points in datas:

    t.up()
    t.goto(points[0], points[1]) # x, y 좌표 설정
    t.down()
    t.fillcolor(points[2]) # 색상 설정
    t.begin_fill() # 채색 시작

    for num in range(2, len(points)): # 회전하면서 그리기

        t.forward(50)
        t.left(points[num])

t.end_fill() # 채색 끝



# 사용자가 입력한 만큼 도형 각을 그리기

import turtle 

t = turtle.Turtle()
t.shape('turtle')

userInput = int(input('몇 각형을 그리겠습니까? : '))

for i in range(userInput):

    t.forward(5)

    start = 180 - ((180 * (n - 2)) / n)
    
    t.left(start)



# 수학 시험 프로그램

Quiz = (['3+2', 5, 3], ['5 / 2의 몫', 2, 5], ['10-2', 8, 3], ['10^2*2', 200, 5], ['1-(10/4의 나머지', -1, 5], ['2^4', 16, 3], ['4/2', 2, 3])

answerCount = 0
wrongAnswerCount = 0
totalScore = 0

for item in Quiz:

    print('문제 : ', item[0])

    answer = int(input('정답을 입력하세요 : '))

    if answer == item[1]:

        answerCount += 1

        totalScore += item[2]

    else:

        wrongAnswerCount += 1

print('-' * 30)
print('정답 개수\t : ', answerCount)
print('오답 개수\t : ', wrongAnswerCount)
print('Total Score\t : ', totalScore)
print('-' * 30)

'''