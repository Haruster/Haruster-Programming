# pass 키워드를 사용하여 에러 발생 방지

'''
pass키워드 : 프로그램에서 조건문을 코딩할 때 실행문이 아직 정해지지 않은 경우에 사용한다.

- 필요한 문장이 없는 경우 프로그램을 다음 단계로 넘기는 역할을 한다.

'''

score = int(input('점수를 입력하세요 : '))

if score >= 80:

    pass # 80이상인 경우 실행문

else:

    pass # 80미만인 경우 실행문