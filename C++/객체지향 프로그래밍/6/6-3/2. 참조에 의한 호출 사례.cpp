// 참조에 의한 호출 사례

#include <iostream>

using namespace std;

void swap(int &a, int &b) { // 참조 변수 a, b

    int tmp;

    tmp = a;

    a = b; // 참조 매개 변수를 보통 변수 처럼 사용한다.
    b = tmp;

}

int main() {

    int m = 2;
    int n = 9;

    swap(m, n); // 함수가 호출되면 m, n에 대한 참조 변수 a, b가 생긴다.

    cout << m << ' ' << n;

}