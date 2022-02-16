# 기상 예보 프로그램 error -2

def forecast(t, h ,r):

    print('온도 : ', t, '도')
    print('습도 : ', h, '%')
    print('비올 확률 : ', r, '%')

temp = 32
hum = 67
rain = 50

forecast(hum, rain, temp)