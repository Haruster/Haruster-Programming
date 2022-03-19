// C-스트링을 이용하여 암호가 입력되면 프로그램을 종료

#include <iostream>
#include <cstring> // strcmp()를 사용하기 위한 헤더 파일이다.

using namespace std;

int main() {

    char password[10];

    cout << "프로그램을 종료하려면 암호를 입력하세요 : " << endl;

    while (true) {

        cout << "암호 >>" << endl;

        cin >> password;

        if (strcmp(password,  "C++") == 0) {

            cout << "프로그램을 정상 종료합니다." << endl;

            break;

        }

        else {

            cout << "암호가 틀립니다. 다시 실행해주세요 " << endl;

        }

    }

    return 0;

}