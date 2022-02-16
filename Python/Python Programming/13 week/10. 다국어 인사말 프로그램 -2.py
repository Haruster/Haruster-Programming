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