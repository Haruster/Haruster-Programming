# 모든 피연산자가 True일 때만 결과는 True
num1 = 10
num2 = 20
num3 = 30

print((num1 < num2) and (num2 < num3) and (num3 > num1)) # True가 출력됨

print((num1 < num2) and (num2 < num3) and (num3 < num1)) # False가 출력됨

print((num1 > num2) and (num2 > num3) and (num3 < num1)) # False가 출력됨