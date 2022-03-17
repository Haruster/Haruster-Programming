// 키보드에서 문자열 입력받고 출력하기

#include <iostream>

using namespace std;

int main() {

    char name[8];

    cout << "이름을 입력해주세요 : " << endl;

    cin >> name;

    int age;

    cout << "나이를 입력해주세요 : " << endl;

    cin >> age;

    char addr[7];

    cout << "사는 지역을 입력해주세요 : " << endl;

    cin >> addr;

    cout << "당신의 이름은 " << name << "나이는 " << age << "사는 곳은 " << addr << "입니다." << endl;

    return 0;

}