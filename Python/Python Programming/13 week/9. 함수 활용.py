# 함수 활용

def printMemberInfo():

    getMemberInDB()
    print('회원정보를 출력한다.')

def getMemberInDB():

    connectDB()
    selectMemberInDB()
    print('데이터베이스에서 회원정보를 가져온다.')

def connectDB():

    print('데이터베이스에 접속한다.')

def selectMemberInDB():

    print('데이터베이스에서 회원정보를 검색한다.')

printMemberInfo()