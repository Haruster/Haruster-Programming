# 1부터 100까지의 숫자 중 5또는 7의 배수를 제외한 나머지 정수를 출력하는 프로그램

for num in range(1, 101): # 1부터 100까지 1씩 증가

    if num % 5 == 0 or num % 7 == 0:

        continue

    print(num)