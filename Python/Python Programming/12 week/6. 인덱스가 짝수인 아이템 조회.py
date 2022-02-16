# 인덱스가 짝수인 아이템 조회

sports = ('태권도', '야구', '농구', '배구', '양궁')

for idx, item in enumerate(sports):

    if idx % 2 == 0:

        print(idx, ' : ', item)