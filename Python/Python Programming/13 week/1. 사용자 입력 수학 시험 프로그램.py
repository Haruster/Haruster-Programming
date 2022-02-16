# 사용자 입력 수학 시험 프로그램 

quiz = []

for i in range(2):

    quiz.append([])
    quiz[i].append(input('문제를 입력해주세여 : '))
    quiz[i].append(int(input('정답 입력 : ')))
    quiz[i].append(int(input('배점 입력 : ')))

quiz = tuple(quiz)

answerCount = 0
wrongAnswerCount = 0
totalScore = 0

for item in quiz:
    
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