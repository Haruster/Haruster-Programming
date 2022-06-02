// 함수 중복의 약점 - 중복 함수의 코드 중복

#include <iostream>

using namespace std;

void myswap(int& a, int& b) {

    int tmp;

    tmp = a;

    a = b;

    b = tmp;

}

void myswap(double& a, double& b) {


    double tmp;

    tmp = a;

    a = b;

    b = tmp;

}

int main() {

    int a = 4, b = 5;

    myswap(a, b);   // myswap(int& a, int& b) 호출

    cout << a << '\t' << b << endl;

    double c = 0.3, d = 12.5;

    myswap(c, d);   // myswap(double& a, double& b) 호출

    cout << c << '\t' << d << endl;

}