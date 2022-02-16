# 1 ~ 10까지의 정수 중 홀수만 더하기(continue 키워드 사용)

for num in range(1, 11): #1부터 10까지 1씩 증가

    if num % 2 == 0: 
        continue # 짝수는 생략
    print(num)