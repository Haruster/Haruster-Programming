'''

# 변수에 값 대입하기

v1 = input('첫 번째 수 입력 : ')
v2 = input('두 번째 수 입력 : ')

temp = v1
v1 = v2
v2 = temp

print(v1, v2)


# 1분기 매출액 구하기

sales1 = int(input('1월 매출 : '))
sales2 = int(input('2월 매출 : '))
sales3 = int(input('3월 매출 : '))

total = sales1 + sales2 + sales3

print("1분기 전체 매출 :", total, "원")


# 덧셈 (실수형)

num1 = 3.14
num2 = 0.5

result = num1 + num2

type(result)

print(result)


# 덧셈 결과값의 자료형 
# 정수 + 정수 = 정수형(int)

num1 = 10
num2 = 20
result = num1 + num2

type(result)
print(result)


# 문자열 연산

str1 = 'hello'
str2 = ' '
str3 = 'world'

str_total = str1 + str2 + str3

print(str_total)


# 문자열 - 확인 문제

num1 = 3.14
num2 = 0.25
result = num1 + num2

print(result)
print(int(result))
print(float(result))


# 1분기 수익 계산하기

sales = int(input('1분기 매출 : ')) # 매출 입력

purchase = int(input('1분기 매입 : ')) # 매입 입력

profit = sales - purchase # 수익 계산

print('수익 :', profit, '원')


# 변수 뺄셈

num1 = 20
num2 = 10

result = num1 = num2

print(result)


# 변수 곱셈
# 두 개의 피연산자를 곱하는 곱셈 연산은 *를 사용한다.
num1 = 20
num2 = 5

result = num1 * num2

print(result)


# 문자열 곱셈
# 문자열 * 양의 정수 = 문자열을 곱한 숫자만큼 반복한다.

result = 'a' * 3

print(result)



# 문자열 곱셈
# Good morning이라는 문자열을 사용자가 입력한 숫자만큼 반복해서 출력하기

Data = int(input("원하는 출력 횟수를 입력하세요 : "))
result = 'Good morning' * Data

print(result)


# 나눗셈 
# 나눗셈 연산은 '/'을 사용한다.
# 문자열의 나눗셈은 불가능하다.

num1 = 100
num2 = 10

result = num1 / num2

print(result)


# 신체질량지수(BMI) 구하기

weight = float(input('몸무게(kg) : ')) # 몸무게 입력

height = float(input('신장(m) : ')) # 신장 입력

bmi = int(weight / (height * height))

print('BMI : ', bmi)


# 나머지 구하기
# 나머지를 구하는 연산자로 %를 사용한다.

num1 = 10
num2 = 4

result = num1 % num2

print(result)


# 홀짝 게임

inputData = int(input('손 안에 동전 수를 입력하세요. '))

result = inputData % 2

print(result)


# 몫 구하기
# 몫을 구하는 연산자로 '//'를 사용한다.

num1 = 10
num2 = 3

result = num1 // num2

print(result)


# 빵을 나누어줄 수 있는 사람 수 구하기

bread = 97
count = 3
maxCount = bread // count

print('빵을 나누어 줄 수 있는 사람 수 : ', maxCount)

rest = bread % count

print('남는 빵 개수 : ', rest)


# 거듭제곱 구하기
# 거듭제곱을 구하는 연산자로는 **를 사용한다.
# 왼쪽 피 연산자에 대한 오른쪽 피연잔자의 거듭제곱을 계산한다.

num1 = 2
num2 = 4

result = num1 ** num2

print(result)


# 전염병 예상 감염자 수 구하기

man = 2 # 1일차 감염자 수

data = 30

total = man ** data

print("30일 이후 예상 감염자 수 : ", total)

'''

# 복리 계산기 만들기 (할당 연산자 사용)

myMoney = 5000000

rate = 0.05

myMoney += myMoney * rate # 1년 후 총 금액

myMoney += myMoney * rate # 2년 후 총 금액

myMoney += myMoney * rate # 3년 후 총 금액

myMoney += myMoney * rate # 4년 후 총 금액  

myMoney += myMoney * rate # 5년 후 총 금액

print("5년 후 총 수령액 : ", int(myMoney), "원")
