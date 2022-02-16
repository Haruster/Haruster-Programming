Quiz = []


for j in range(3):

    line = []

    print(j + 1,'번째 문제의 문제, 정답, 배점을 입력해주세요 :')

    for i in range(1):

        line.append(input())
        line.append(int(input()))
        line.append(int(input()))
        
    Quiz.append(line)

Quiz = tuple(Quiz) # 리스트를 튜플로 데이터 타입 변환

print('문제 : ', Quiz)


answerCount = 0
wrongAnswerCount = 0
totalScore = 0

for item in Quiz:

    print('문제 : ', item[0])

    answer = int(input('정답을 입력하세요 : '))

    if answer == item[1]:

        answerCount += 1

        totalScore += item[2]

    else:

        wrongAnswerCount += 1

print('-' * 30)
print('정답 개수\t : ', answerCount)
print('오답 개수\t : ', wrongAnswerCount)
print('Total Score\t : ', totalScore)
print('-' * 30)

print(type(Quiz)) # 타입 출력
