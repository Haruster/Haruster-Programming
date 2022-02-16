# 구구단 전체 출력(한줄로)

for n1 in range(1, 10, 1): # 1부터 9까지 1씩 증가
    for n2 in range(2, 10, 1): # 2부터 9까지 1씩 증가

        print(f'{n1} x {n2} = {n1 * n2}')

    print()