# 리스트와 튜플간 변환

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

print('colors의 자료형 : ', type(colors)) # colors의 자료형 출력

colors = list(colors) # 튜플을 리스트로 데이터 타입 변환
print('colors의 자료형 : ', type(colors))

colors = tuple(colors) # 리스트를 튜플로 데이터 타입 변환
print('colors의 자료형 : ', type(colors))