# 복리 계산기 만들기 (할당 연산자 사용)

myMoney = 5000000

rate = 0.05

myMoney += myMoney * rate # 1년 후 총 금액

myMoney += myMoney * rate # 2년 후 총 금액

myMoney += myMoney * rate # 3년 후 총 금액

myMoney += myMoney * rate # 4년 후 총 금액  

myMoney += myMoney * rate # 5년 후 총 금액

print("5년 후 총 수령액 : ", int(myMoney), "원")
