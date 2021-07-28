'''
if문 구조

if 조건1:    # 첫번째 조건
	실행문1
elif 조건2: #추가되는 조건
	실행문2
else:	# 예외(마지막)
	실행문3
'''

x = 1

if x < 3:
	print("1")
elif x == 3:
	print("3")
elif x == 2:
	print("2")
else:
	print("data error")
