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