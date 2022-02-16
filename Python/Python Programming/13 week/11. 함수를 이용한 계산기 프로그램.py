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