class MemberInfo:
    
    def Setinfo(self, name, age, addr): # 클래스 내부에 정의 되어있는 함수를 메소드라고 부른다.
        
        self.name = name
        self.age = age
        self.addr = addr
        
member1 = MemberInfo()