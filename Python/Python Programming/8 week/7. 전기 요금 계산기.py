# 전기 요금 계산 프로그램

basicPrice = 0 # 기본 요금
unitPrice = 0 # 단가
totalPrice = 0 # 전기 요금

amount = float(input('전기 사용량을 입력하세요. : '))

if amount > 400:

    basicPrice = 7300
    unitPrice = 280.6

elif amount > 201:
    basicPrice = 1600
    unitPrice = 187.9

else:

    basicPrice = 910
    unitPrice = 99.3

totalPrice = amount + unitPrice + basicPrice

print('사용량 : ', amount, 'kwh')
print('기본요금 : ', basicPrice, '원')
print('단가 : ', unitPrice, '원')
print('전기 요금 : ', totalPrice, '원')


