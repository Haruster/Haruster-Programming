// 객체 리턴

#include <iostream>

using namespace std;

class Circle {

    int radius;

public:

    Circle() {radius = 1;}
    Circle(int radius) {this -> radius = radius;}

    void setRadius(int radius) {this -> radius = radius;}

    double getArea() {return 3.14 * radius * radius;}

};

Circle getCircle() {

    Circle tmp(30);

    return tmp; // 객체 tmp를 리턴한다.

}

int main() {

    Circle c; // 객체가 생성되며, radius = 1로 초기화된다.

    cout << c.getArea() << endl;

    c = getCircle(); // tmp객체가 c에 복사되며, c의 radius는 30이 된다.

    cout << c.getArea() << endl;

    return 0;

}