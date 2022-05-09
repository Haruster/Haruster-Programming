#include <iostream>
#include <string>

using namespace std;


void msg(int id) {

    cout << id << endl;

}

void msg(int id, string s = "") {

    cout << id << ":" << s << endl;

}

int main() {

    msg(5, "Good Morning");     // 정상 컴파일. 두 번째 msg() 호출

    msg(6);     // 한수 호출 모호. 컴파일

}   