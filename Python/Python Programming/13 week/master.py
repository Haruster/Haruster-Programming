# 사용자 입력 수학 시험 프로그램 

quiz = []

for i in range(2):

    quiz.append([])
    quiz[i].append(input('문제를 입력해주세여 : '))
    quiz[i].append(int(input('정답 입력 : ')))
    quiz[i].append(int(input('배점 입력 : ')))

quiz = tuple(quiz)

answerCount = 0
wrongAnswerCount = 0
totalScore = 0

for item in quiz:
    
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
# 대표적인 내장 함수(print, len등)

userName = "Hong gil dong"

print('이름 : ', userName)
print('이름의 길이 : ', len(userName))

# print() 함수는 무언가를 출력하는 함수이고, len() 함수는 문자열의 길이를 구하는 함수이다. 

# 사용자 정의 함수를 이용하여 온도센서 작동 시스템 만들기

def startTemperatureSensor():

    print('온도센서의 작동을 시작합니다.')

def stopTemperatureSensor():

    print('온도센서의 작동을 중지합니다.')

startTemperatureSensor()
stopTemperatureSensor()


# 사용자 정의 함수를 정의하고 호출하기

def greet(): # 함수 정의

    print('Hello.')
    print('Nice to meet you')

greet() # 함수 호출 


# 사용자 정의 함수를 정의하고 호출하기 -2

def greet(): # 함수 정의

    print("Hello.")
    print('Nice to meet you')

greet()
greet()
greet()


# 노트북 인치 구하기

def convertUnit():

    print(lengthCm, 'cm = ', lengthCm * 0.393701, 'inch')

lengthCm = float(input('길이를 입력하세요.(cm)'))

convertUnit()


# 이동 거리를 계산하는 함수

def calculateDistance():

    print('이동 거리는 ', hourData * speedData, 'km입니다.')

hourData = float(input('이동 시간을 입력하세요. : '))
speedData = float(input('이동 속도를 입력하세요 : '))

calculateDistance()


# 함수에서 pass 키워드 사용

def getMemberInDatabase():

    pass

def sendMemberIdByEmail():

    pass 

m_name = input('이름을 입력하세요. : ')
m_mail = input('메일 주소를 입력하세요. :')

getMemberInDatabase()
sendMemberIdByEmail()


# 함수 내에서 또 다른 함수 호출

def fun1():

    print('fun1 함수를 호출합니다.')

def fun2():

    print('fun2 함수를 호출합니다.')

def fun3():

    fun1()
    fun2()
    print('fun3 함수를 호출합니다.')

fun3()


# 함수 활용

def printMemberInfo():

    getMemberInDB()
    print('회원정보를 출력한다.')

def getMemberInDB():

    connectDB()
    selectMemberInDB()
    print('데이터베이스에서 회원정보를 가져온다.')

def connectDB():

    print('데이터베이스에 접속한다.')

def selectMemberInDB():

    print('데이터베이스에서 회원정보를 검색한다.')

printMemberInfo()


# 다국어 인사말 프로그램

def introKor():

    print('안녕')

def introEng():

    print('Hello.')

def introJap():

    print('こんにちは')

selectNum = int(input('where are you from? 1. 한국, 2. USA, 3. Japan'))

if (selectNum == 1):

    introKor()

elif(selectNum == 2):

    introEng()

elif(selectNum == 3):

    introJap()

else:

    introEng()



# 다국어 인사말 프로그램 -2

def introKor():

    print('안녕')

def introEng():

    print('Hello.')

def introJap():

    print('곤니치와')

selNum = int(input('어디서왔니? 1. 한국, 2. USA, 3. Japan'))

if (selNum == 1):

    introKor()

elif(selNum == 2):

    introEng()

elif(selNum == 3):

    introJap()

else:

    introEng()



# 함수를 이용한 계산기 프로그램

def add(): # 덧셈

    print('덧셈 결과 : ', inputNumber1 + inputNumber2)

def sub(): # 뺄셈

    print('뺄셈 결과 : ', inputNumber1 - inputNumber2)

def mul(): # 곱셈

    print('곱셈 결과 : ', inputNumber1 * inputNumber2)

def div(): # 나눗셈

    print('나눗셈 결과 : ', inputNumber1 / inputNumber2)    

def calculator(): # 계산기

    if(selectOperator == 1):

        add()

    elif(selectOperator == 2):

        sub()

    elif(selectOperator == 3):

        mul()

    elif(selectOperator == 4):

        div()

inputNumber1 = float('숫자를 입력하세요. : ')
selectOperator = int(input('연산자를 선택하세요. 1. 덧셈, 2. 뺄셈, 3. 곱셉, 4. 나눗셈'))
inputNumber2 = float('숫자를 입력하세요. : ')

calculator()



# 전역 변수

num = 10 # 전역 변수 num 선언

def fun1():

    print('num : ', num) # 전역 변수 num 사용

print('num : ', num) # 전역 변수 num 사용
fun1()


# 전역 변수와 지역 변수의 차이

num = 10 # 전역 변수 num 선언

def fun1(): # 함수 정의

    num = 20 # 지역 변수 num 선언
    print('num : ', num) # 지역 변수 num 사용(함수 안에서 num을 먼저 찾는다.)

print('num : ', num) # 전역 변수 num 사용
fun1() # 함수 호출


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



# 웹 사이트의 누적 방문 횟수 프로그램

flag = True
totalVisitor = 0

def countVisitor(): # 함수 정의

    global totalVisitor  # 전역 변수 설정
    totalVisitor += 1

while flag:

    inputData = int(input('1. 웹 사이트 방문, 2. 종료'))

    if inputData == 1:

        countVisitor() # 함수 호출

        print('누적 방문 횟수 : ', totalVisitor)

    else:

        flag = False



# 웹 사이트의 누적 방문 횟수 프로그램 error -1

flag = True
totalVisitor = 0

def countVisitor(): # 함수 정의

    totalVisitor  # 전역 변수 설정
    totalVisitor += 1

while flag:

    inputData = int(input('1. 웹 사이트 방문, 2. 종료'))

    if inputData == 1:

        countVisitor() # 함수 호출

        print('누적 방문 횟수 : ', totalVisitor)

    else:

        flag = False



# 웹 사이트의 누적 방문 횟수 프로그램 error -2

flag = True
totalVisitor = 0

def countVisitor(): # 함수 정의

    totalVisitor = 0  # 전역 변수 설정
    totalVisitor += 1

while flag:

    inputData = int(input('1. 웹 사이트 방문, 2. 종료'))

    if inputData == 1:

        countVisitor() # 함수 호출

        print('누적 방문 횟수 : ', totalVisitor)

    else:

        flag = False


# 인수와 매개변수의 사용

def greet(name): # name이라는 매개변수 선언

    print(name, '씨 안녕하세요.')

greet('홍길동') # '홍길동'이라는 인수를 매개변수에 전달하여 출력
greet('박찬호') # '박찬호'이라는 인수를 매개변수에 전달하여 출력
greet('박지성') # '박지성'이라는 인수를 매개변수에 전달하여 출력


# 여러개의 매개변수 선언

def forecastWeather(temp, humi, rain): # 함수 정의, 인수 3개를 매개변수에 저장

    print('날씨 예보입니다.')
    print('최고 온도 : ', temp, '도')
    print('평균 습도 : ', humi, '%')
    print('비올 확률 : ', rain, '%')

temperature = 32
humidity = 67
rainPercent = 50

forecastWeather(temperature, humidity, rainPercent) # 함수 호출 시 인수 3개 전달


# 기상 예보 프로그램 

def forecast(t, h ,r):

    print('온도 : ', t, '도')
    print('습도 : ', h, '%')
    print('비올 확률 : ', r, '%')

temp = 32
hum = 67
rain = 50

forecast(temp, hum, rain)


# 기상 예보 프로그램 error -1

def forecast(t, h ,r):

    print('온도 : ', t, '도')
    print('습도 : ', h, '%')
    print('비올 확률 : ', r, '%')

temp = 32
hum = 67
rain = 50

forecast(temp, hum)



# 기상 예보 프로그램 error -2

def forecast(t, h ,r):

    print('온도 : ', t, '도')
    print('습도 : ', h, '%')
    print('비올 확률 : ', r, '%')

temp = 32
hum = 67
rain = 50

forecast(hum, rain, temp)
'''