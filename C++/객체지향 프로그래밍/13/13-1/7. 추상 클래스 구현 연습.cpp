// 추상 클래스 구현 연습

#include <iostream>

using namespace std;

// 이 곳에 Calculator 클래스 코드 필요

class GoodCalc : public Calculator {

public:

    int add(int a, int b) { return a + b; }
    int subtract(int a, int b) { return a - b; }

    double average(int a [], int size) {

        double sum = 0;

        for (int i = 0; i < size; i++) {

            sum += a[i];

        }

        return sum / size;

    }

};

int main() {

    int a[] = {1, 2, 3, 4, 5};

    Calculator *p = new GoodCalc;

    cout << p->add(2, 3) << endl;
    cout << p->subtract(2, 3) << endl;
    cout << p->average(a, 5) << endl;

    delete p;

}