# score가 점수에 상관없이 모두 D를 출력
'''
요구 사항에 맞는 프로그램 만들기
- if-elif문을 이용해서 다중 비교를 하더라도 실제로 실행되는 실행문은 하나뿐이거나 아예 없을 수 있다.
-> 따라서 적절한 조건식의 순서 설계가 필요하다.
'''

score = int(input('점수를 입력하세요 : '))

if score >= 60: # 60점 이상이면 'D' 출력
    print('D')

elif score >= 80:
    print('B')

elif score >= 70:
    print('C')

elif score >= 90:
    print('A')

else:
    print('F')