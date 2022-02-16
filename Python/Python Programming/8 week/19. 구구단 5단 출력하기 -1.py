# 구구단 5단 출력하기 -1

for num in range(1, 10, 1): # 1부터 9까지 1씩 증가
    print(5, end = '')
    print(' * ', end = '')
    print(num, end = '')
    print(' = ', end = '')
    print(5 * num)