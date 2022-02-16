# 딕셔너리에 아이템 수정

dicContainer = {'이름' : '홍길동', '나이' : 25, '주소' : '서대문구 연희로', '취미' : ['축구', '수영', '조깅'], '몸무게' : 85.3} # 딕셔너리 선언

dicContainer['몸무게'] = 90 # '몸무게'에 해당하는 아이템 수정

dicContainer['나이'] = dicContainer['나이'] + 1

print(dicContainer) # 딕셔너리 출력