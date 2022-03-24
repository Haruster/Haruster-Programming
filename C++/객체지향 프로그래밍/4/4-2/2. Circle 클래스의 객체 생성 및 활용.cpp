#include <iostream>

using namespace std;

// Circle 선언부
class Circle {

    public:
        int radius;
        double getArea();

};

// Circle 구현부
double Circle :: getArea() {

    return 3.14 * radius * radius; 

}

int main() {

    Circle donut; // 객체 donut 생성
 
    donut.radius = 1; // donut 객체의 반지름을 1로 설정(donut의 멤버 변수 접근)

    double area = donut.getArea(); // donut 객체의 면적 알아내기 (donut의 멤버 함수 호출)
    
    cout << "donut의 면적은 " << area << endl;

    Circle pizza; // 객체 pizza 생성

    pizza.radius = 30; // pizza 객체의 반지름을 30으로 설정(pizza의 멤버 변수 접근)

    area = pizza.getArea(); // pizza 객체의 면적 알아내기 (pizza의 멤버 함수 호출)

    cout << "Pizza의 면적은 " << area << endl;

 
}