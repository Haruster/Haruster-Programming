import operator

targetIncome = 4000000
targetOther = 2

income = int(input('월 소득을 입력하세요. '))
other = int(input('다른 지원금을 받고 있습니까? 1: 받고 있다. 2: 받고 있지 않다. '))

result = '수급 대상자' if operator.and_(operator.le(income, targetIncome), operator.eq(other, targetOther)) else '수급 비대상자'

print(result)