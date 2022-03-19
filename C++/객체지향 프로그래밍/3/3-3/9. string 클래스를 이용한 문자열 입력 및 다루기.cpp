// string 클래스를 이용한 문자열 입력 및 다루기

#include <iostream>
#include <string> // string 클래스를 만들기 위한 헤더파일

using namespace std;

int main() {

    string song("Falling in love with you"); // 문자열 song
    string elvis("Elvis Presley"); // 문자열 elvis
    string singer; // 문자열 singer

    cout << song + "를 부른 가수는 " << endl; // +로 문자열 연결
    cout << "(힌트 : 첫 글자는 " << elvis[0] << ")?" << endl; // []연산자 사용

    getline(cin, singer); // 문자열 입력

    if (singer == elvis) {// 문자열 비교

        cout << "정답입니다." << endl;

    }

    else {

        cout << "틀렸습니다. 정답은 " << elvis + "입니다." << endl;

    }

    return 0;
}