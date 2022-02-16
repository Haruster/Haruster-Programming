# 사용자가 원하는 곳에서 사용자가 원하는 값까지 구하기

sum = 0

start = int(input('몇부터 더할까요? : '))
limit = int(input('몇까지 더할까요? : '))

for num in range(start, limit + 1, 1): # start부터 limit + 1까지 1씩 증가

    sum = sum + num

print('sum = %d' %sum)