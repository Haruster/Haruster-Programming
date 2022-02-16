# score가 점수에 상관없이 모두 'D'를 출력하게 하기

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