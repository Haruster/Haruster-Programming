// 값에 의한 호출 시 매개 변수의 생성자가 실행되지 않음

#include <iostream>

using namespace std;

class Circle {

    private:

        int radius;

    public:

        Circle();
        Circle(int r);
        ~Circle();

        double getArea() {return 3.14 * radius * radius; }

        int getRadius() {return radius;}

        void setRadius(int radius) {this->radius = radius};

}

Circle::Circle() {

    radius = 1;

    cout << "생성자 실행 radius = " << radius << endl; 

}

Circle::Circle(int radius) {

    this->radius = radius;

    cout << "생성자 실행 radius = " << radius << endl;

}

Circle::~Circle() {

    cout << "소멸자 실행 radius = " << radius << endl;

}

void increase(Circle c) {

    int r = c.getRadius();

    c.setRadius(r + 1);

}

int main() {

    Circle Waffle(30);

    increase(Waffle);

    cout << Waffle.getRadius() << endl;

    return 0;

}