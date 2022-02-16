# keys()함수로 조회한 키와 for문을 이용하여 각 키에 해당하는 값을 출력

dicContainer = {'이름' : '홍길동', '나이' : 25, '주소' : '서대문구 연희로', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

print(dicContainer) # 딕셔너리 출력

for key in dicContainer.keys(): # key에 해당하는 값 출력

    print(key, '\t: ', dicContainer[key])