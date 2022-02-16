# 신체질량지수(BMI) 구하기

weight = float(input('몸무게(kg) : ')) # 몸무게 입력

height = float(input('신장(m) : ')) # 신장 입력

bmi = int(weight / (height * height))

print('BMI : ', bmi)