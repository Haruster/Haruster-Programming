// cin.getline()을 이용한 문자열 입력

#include <iostream>
#include <cstring>

using namespace std;

int main(void) {

    cout << "주소를 입력하세요 : " << endl;

    char address[100]; // 배열 크기가 100인 문자형 변수 char 선언

    cin.getline(address, 100, '\n'); // 키보드로부터 값 읽기

    cout << "주소는" << address << "입니다." << endl; // 주소 출력

    return 0;

}