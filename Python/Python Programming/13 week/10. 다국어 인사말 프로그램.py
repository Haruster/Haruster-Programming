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