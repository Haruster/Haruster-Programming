# 자료형 변환
# 문자형을 논리형으로 변환하기 
# - 빈 문자("")를 논리형으로 바꾸면 False로 변환되고, 그 외 나머지 문자는 모두 True로 변환됨.
# 공백 문자('')도 True로 변환됨

myVar = 'Hello'
type(myVar)

myVar = bool(myVar)

type(myVar)

print(myVar)