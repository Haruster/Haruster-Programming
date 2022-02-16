# 인덱스가 홀수인 아이템 조회 -2

sports = ('태권도', '야구', '농구', '배구', '양궁')

for idx, item in enumerate(sports):

    if idx % 2 == 1:

        print(idx, ' : ', item)