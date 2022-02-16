# BMI 프로그램

'''
BMI 지수를 입력한다.
BMI 지수가 90 이하면 '저체중'을 입력한다.
BMI 지수가 90 초과 ~ 110 이하면 '정상체중'을 출력한다.
BMI 지수가 110 초과 ~ 120 이하면 '과체중'을 출력한다.
BMI 지수가 120 초과 ~ 140 이하면 '비만'을 출력한다.
BMI 지수가 140 초과면 '고도비만'을 출력한다.
'''

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