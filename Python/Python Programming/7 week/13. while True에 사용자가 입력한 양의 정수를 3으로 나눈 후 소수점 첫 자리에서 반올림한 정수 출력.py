# while True에 사용자가 입력한 양의 정수를 3으로 나눈 후 소수점 첫 자리에서 반올림한 정수 출력

while True:

    number = int(input('양의 정수 입력 : ')) # 사용자가 양의 정수 임력

    result = number / 3 # 3으로 나눈다.

    if (result - int(result)) >= 0.5: # 소수 첫 번째 자리ㅏ 5이상이면

        result = int(result) + 1 # 올림

    else:

        result = int(result) # 버림

    print('결과 : ', result) # 반올림한 결과 출력