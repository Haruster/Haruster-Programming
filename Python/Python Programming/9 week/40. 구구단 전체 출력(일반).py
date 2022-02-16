# 구구단 전체 출력(일반)

for n1 in range(1, 10, 1): # 1부터 9까지 1씩 증가
    for n2 in range(2, 10, 1): # 2부터 9까지 1씩 증가
        print(n2, end = '')
        print(' x ', end = '')
        print(n1, end = '')
        print(' = ', end = '')
        print(n2 * n1, '\t', end = '')

    print()
