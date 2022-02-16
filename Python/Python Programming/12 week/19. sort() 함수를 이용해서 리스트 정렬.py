# sort() 함수를 이용해서 리스트 정렬

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

cs = sorted(colors)

cs.sort(reverse = True) # 내림차순
print(cs)

cs.sort(reverse = False) # 오름차순
print(cs)

