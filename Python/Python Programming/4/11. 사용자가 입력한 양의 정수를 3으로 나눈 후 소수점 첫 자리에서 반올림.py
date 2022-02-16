# 사용자가 입력한 양의 정수를 3으로 나눈 후 소수점 첫 자리에서 반올림

number = int(input('양의 정수 입력 : '))# 사용자가 양의 정수 입력

result = number / 3

if (result - int(result)) >= 0.5:

    result = int(result) + 1

else:

    result = int(result)


print('결과 : ', result)