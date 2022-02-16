# if elif else문을 사용하여 요구사항에 맞는 프로그램 작성

score = int(input('점수를 입력하세요 : '))

if score >= 90: # 점수가 90점 이상이면 'A'출력

    print('A')

elif score >= 80: # 점수가 90점 미만 80점 이상이면 'B' 출력

    print('B')

elif score >= 70: # 점수가 80점 미만 70점 이상이면 'C' 출력

    print('C')

elif score >= 60: # 점수가 70점 미만 60점 이상이면 'D' 출력

    print('D')

else: # 점수가 60점 미만임년 'F'를 출력

    print('F')