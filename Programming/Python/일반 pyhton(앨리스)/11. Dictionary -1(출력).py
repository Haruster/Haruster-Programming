# Dictionary(딕셔너리) : 짝궁이 있는 자료형이다.
    # {key: value}의 형식 : Key를 알면 Value를 알 수 있음.
        # Key : 열쇠처럼 자료를 꺼낼 수 있는 도구.
        # Value : Dictionary에서 Key로 꺼낸 자료.

# Key는 변할 수 없는 자료형이여야 한다. (리스트는 안되고 튜플은 된다.)

dict_zero = {}

person = {'name': 'Kiensys', 'age': 20}

#자료 출력 -> print(Dictionary['key'])

print(person['name']) # Kinesys가 출력됨.
print(person['age']) # 20이 출력됨.