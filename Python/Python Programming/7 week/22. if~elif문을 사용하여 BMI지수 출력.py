# if~elif문을 사용하여 BMI 지수 출력

bmi = int(input('BMI 지수를 입력하세요. '))

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